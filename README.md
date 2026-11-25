# Compute Evoked Responses from Epoched Data

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Computes evoked responses from epoched MEG/EEG data with MNE-Python Epochs.average, optionally one per event type, and outputs an MNE evoked file, a figure and an HTML report.**

Loads MNE epochs and averages them with mne.Epochs.average using the chosen channel picks and combination method (mean or median), either all together or separately for each condition. Produces ave.fif, a plot of the evoked response and an HTML QC report. Use it after epoching (and artifact rejection) to obtain ERPs/ERFs for later analyses.

| | |
|---|---|
| 📥 **Inputs** | `neuro/meeg/mne/epochs` |
| 📤 **Outputs** | `neuro/meeg/mne/evoked` · `report/html` |
| 🐳 **Container** | `brainlifemeeg/mne:1.12.1` |
| ⚙️ **Resources** | 1 CPUs · 3 GB memory |
| 🔗 **Run it** | [doi.org/10.25663/brainlife.app.618](https://doi.org/10.25663/brainlife.app.618) |

#### 📥 Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `fif` | `neuro/meeg/mne/epochs` | yes | Epoched MEG/EEG data (MNE -epo.fif). |

#### 📤 Outputs

| Output | Datatype | Description |
|---|---|---|
| `out_dir` | `neuro/meeg/mne/evoked` | Evoked response(s) in MNE format (ave.fif), one per condition when by_event_type is true. |
| `out_dir_report` | `report/html` | HTML report (report.html) with the evoked response visualisations. |

<details>
<summary><b>⚙️ Parameters</b> (3)</summary>

| Parameter | Type | Default | Description |
|---|---|---|---|
| `picks` | string |  | The channel type to plot. For 'grad', the gradiometers are collected in pairs and the RMS for each pair is plotted. If None the first available channel type from order shown above is used. Defaults to None. |
| `method` | string | `mean` | How to combine epochs: 'mean' or 'median' (passed to Epochs.average). |
| `by_event_type` | boolean | `true` | If true, one Evoked object is computed per event type (condition); if false, all epochs are averaged together. |

</details>

📚 **References used by this App:**
- Hayashi S., Caron B. A., Heinsfeld A. S. et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. Nature Methods 21, 809-813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)
- Gramfort A. et al. MEG and EEG data analysis with MNE-Python. Frontiers in Neuroscience 7:267 (2013). [doi:10.3389/fnins.2013.00267](https://doi.org/10.3389/fnins.2013.00267)

<!-- brainlife-app:end -->

[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.618-blue.svg)](https://doi.org/10.25663/brainlife.app.618)

## Description

This app computes evoked responses from epoched MEG/EEG data using
[`mne.Epochs.average()`](https://mne.tools/stable/generated/mne.Epochs.html#mne.Epochs.average). Epochs can be
averaged together into a single `Evoked` object, or split `by_event_type` into one `Evoked` object per
condition.

The app generates:
- Evoked data in MNE format (one or more `Evoked` objects)
- A figure of the evoked response(s)
- An HTML report with the evoked visualization(s)
- `product.json` Brainlife.io metadata, including the evoked response image

## Inputs

- **`fif`** (`neuro/meeg/mne/epochs`): epoched MEG/EEG data to average (required)

## Outputs

- **`out_dir/ave.fif`** (`neuro/meeg/mne/evoked`): evoked response(s) in MNE format
- **`out_figs/evoked.png`** (`generic/image/png`): plot of the evoked response, also embedded in `product.json`
- **`out_report/report.html`** (`report/html`): HTML report with the evoked response visualization(s)

## Configuration Parameters

| key | type | default | description |
|---|---|---|---|
| `picks` | string | `""` | Channels to average, passed to `mne.Epochs.average()`: a channel *type* (e.g. `"eeg"`, `"meg"`), specific channel names, `"all"`, or `"data"`. If `None`, all data channels are used. |
| `method` | string | `"mean"` | How to combine the data across epochs: `"mean"`/`"median"`, or any other value is passed through as a callable method name. |
| `by_event_type` | boolean | `true` | When `true`, epochs are grouped by event type and a separate `Evoked` object is returned for each condition. When `false`, all epochs are averaged together into a single `Evoked` object. |

## Usage

### Running on Brainlife.io

1. Upload or select your epoched MEG/EEG data file (`.fif`)
2. Select the evoked-averaged app
3. Configure averaging parameters:
   - Set `picks` to restrict averaging to a channel type or subset (optional)
   - Choose `method` (`"mean"` or `"median"`)
   - Set `by_event_type` to compute one evoked response per condition
4. Submit the task
5. Monitor task completion and review the evoked response in the report viewer

### Local Testing

```bash
# Update config.json with your data path
# Then run:
python main.py
```

## Technical Details

- Built with MNE-Python
- Headless plotting via the matplotlib Agg backend
- Compatible with downstream Brainlife.io MNE apps

## Authors

- Saeed Zahran (https://github.com/zahransa)
- Maximilien Chaumon (https://github.com/dnacombo)

## Citations

- Hayashi, S., Caron, B.A., Heinsfeld, A.S. et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. Nat Methods 21, 809–813 (2024). https://doi.org/10.1038/s41592-024-02237-2
- Gramfort, A. et al. MEG and EEG data analysis with MNE-Python. Front. Neurosci. 7, 267 (2013). https://doi.org/10.3389/fnins.2013.00267

## Funding Acknowledgement

brainlife.io is publicly funded. We kindly ask that you acknowledge the funding below in your code and publications.

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://grantome.com/grant/NIH/R01-EB029272-01)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://grantome.com/grant/NIH/R01-EB030896-01)

## License

Copyright (c) 2026 MEEG Brainlife team. Licensed under AGPL-3.0, see [license.txt](license.txt).
