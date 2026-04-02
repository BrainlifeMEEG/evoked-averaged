"""
Compute evoked responses from epoched MNE data.

This app loads MNE Epochs data and computes evoked responses using configurable
averaging settings. It supports returning one evoked per event type, generates
a QC figure and HTML report, saves evoked data to FIF, and writes Brainlife
product metadata.

Inputs:
    - fif: Path to epoched MNE data (.fif)
    - picks: Channel picks for averaging (optional)
    - method: Averaging method for Epochs.average (e.g., 'mean', 'median')
    - by_event_type: Whether to compute one evoked per event type

Outputs:
    - out_dir/evokeds_ave.fif: Evoked data in MNE format
    - out_figs/evoked.png: Evoked trace figure
    - out_report/report.html: HTML QC report
    - product.json: Brainlife.io product metadata
"""

# Copyright (c) 2026 brainlife.io
#
# This app computes evoked responses from epoched MNE data.
#
# Authors:
# - Saeed Zahran
# - Maximilien Chaumon (https://github.com/dnacombo)

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'brainlife_utils'))

import mne

from brainlife_utils import (
    load_config,
    setup_matplotlib_backend,
    ensure_output_dirs,
    create_product_json,
    add_image_to_product,
    add_info_to_product,
    save_figure_with_base64,
)

# Set up matplotlib for headless execution
setup_matplotlib_backend()

# Ensure output directories exist
ensure_output_dirs('out_dir', 'out_figs', 'out_report')

# Load configuration
config = load_config()

# == LOAD EPOCHS ==
epochs = mne.read_epochs(config['fif'], preload=True)

# == COMPUTE EVOKED ==
evoked = epochs.average(
    picks=config.get('picks'),
    method=config.get('method', 'mean'),
    by_event_type=config.get('by_event_type', False),
)

# == PLOT EVOKED ==
if isinstance(evoked, list):
    fig = evoked[0].plot(spatial_colors=True, show=False)
    first_title = evoked[0].comment
    fig.text(
        0.01,
        0.99,
        f'Evoked response for condition {first_title} (see report for all conditions)',
        horizontalalignment='left',
        verticalalignment='top',
    )
    titles = [ev.comment for ev in evoked]
    n_conditions = len(evoked)
else:
    fig = evoked.plot(spatial_colors=True, show=False)
    fig.text(
        0.01,
        0.99,
        f'Evoked response for condition {evoked.comment}',
        horizontalalignment='left',
        verticalalignment='top',
    )
    titles = evoked.comment
    n_conditions = 1

fig_path = os.path.join('out_figs', 'evoked.png')
fig_base64 = save_figure_with_base64(fig, fig_path, dpi_file=150, dpi_base64=80)

# == CREATE REPORT ==
report = mne.Report(title='Evoked Averaging Report')
report.add_evokeds(evokeds=evoked, titles=titles)
report.save(os.path.join('out_report', 'report.html'), overwrite=True)

# == SAVE DATA ==
mne.write_evokeds(os.path.join('out_dir', 'evokeds_ave.fif'), evoked, overwrite=True)

# == CREATE PRODUCT JSON ==
product_items = []
add_info_to_product(product_items, 'Evoked averaging completed successfully.', msg_type='success')
add_info_to_product(product_items, f'Input epochs: {config["fif"]}')
add_info_to_product(product_items, f'Averaging method: {config.get("method", "mean")}')
add_info_to_product(product_items, f'Conditions in output: {n_conditions}')
add_image_to_product(product_items, 'Evoked response', base64_data=fig_base64)
create_product_json(product_items)

