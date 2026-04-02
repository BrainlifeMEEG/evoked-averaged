# evoked-averaged

[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.530-blue.svg)](https://doi.org/10.25663/brainlife.app.530)

## Description

Computes evoked responses from epoched MNE data using configurable averaging options. The app can average across all epochs or return one evoked object per event type.

## Inputs

- **fif**: MNE epochs file in `.fif` format

## Outputs

- **out_dir/evokeds_ave.fif**: Evoked data in MNE format
- **out_figs/evoked.png**: PNG visualization of evoked traces
- **out_report/report.html**: HTML report with evoked visualizations
- **product.json**: Brainlife.io metadata and preview information

## Configuration Parameters

### Required

- `fif`: Path to input epochs file (`.fif`)

### Optional

- `picks`: Channel picks passed to `mne.Epochs.average()` (e.g., `"eeg"`, `"meg"`, `"data"`)
- `method`: Averaging method (`"mean"`, `"median"`, etc.)
- `by_event_type`: If `true`, computes one evoked per event type

Example configuration:

```json
{
  "fif": "path/to/meg-epo.fif",
  "picks": "",
  "method": "mean",
  "by_event_type": true
}
```

## Usage

The app loads epochs, computes evoked response(s), writes the output `.fif`, generates a figure/report, and creates `product.json`.

## Technical Details

- Built with MNE-Python
- Headless plotting via matplotlib Agg backend
- Compatible with downstream Brainlife.io MNE apps

## Authors

- Saeed Zahran
- [Maximilien Chaumon](https://github.com/dnacombo)

## Citations

Hayashi, S., Caron, B.A., Heinsfeld, A.S. et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. Nat Methods 21, 809–813 (2024). https://doi.org/10.1038/s41592-024-02237-2

Gramfort A, Luessi M, Larson E, Engemann DA, Strohmeier D, Brodbeck C, Goj R, Jas M, Brooks T, Parkkonen L, and Hämäläinen MS. MEG and EEG data analysis with MNE-Python. Frontiers in Neuroscience, 7(267):1–13, 2013. https://doi.org/10.3389/fnins.2013.00267

## Funding

brainlife.io is publicly funded. Please acknowledge the platform in publications using this app.

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://grantome.com/grant/NIH/R01-EB030896-01)

#### MIT Copyright (c) 2026 brainlife.io The University of Texas at Austin and Indiana University
