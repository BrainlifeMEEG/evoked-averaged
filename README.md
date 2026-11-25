<h1 align="center">Compute evoked</h1>

<p align="center">
  Computes evoked responses from epoched MEG/EEG data with MNE-Python Epochs.average, optionally one per event type, and outputs an MNE evoked file, a figure and an HTML report.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/brainlife.app.618"><img src="https://img.shields.io/badge/Brainlife-brainlife.app.618-blue.svg" alt="Run on brainlife.io"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-see_LICENSE-lightgrey.svg" alt="License"></a>
</p>

## At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Computes evoked responses from epoched MEG/EEG data with MNE-Python Epochs.average, optionally one per event type, and outputs an MNE evoked file, a figure and an HTML report.**

Loads MNE epochs and averages them with mne.Epochs.average using the chosen channel picks and combination method (mean or median), either all together or separately for each condition. Produces ave.fif, a plot of the evoked response and an HTML QC report. Use it after epoching (and artifact rejection) to obtain ERPs/ERFs for later analyses.

| | |
|---|---|
| **Inputs** | `neuro/meeg/mne/epochs` |
| **Outputs** | `neuro/meeg/mne/evoked` · `report/html` |
| **Container** | `brainlifemeeg/mne:1.12.1` |
| **Resources** | 1 CPUs · 3 GB memory |
| **Run it** | [doi.org/10.25663/brainlife.app.618](https://doi.org/10.25663/brainlife.app.618) |

#### Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `fif` | `neuro/meeg/mne/epochs` | yes | Epoched MEG/EEG data (MNE -epo.fif). |

#### Outputs

| Output | Datatype | Description |
|---|---|---|
| `out_dir` | `neuro/meeg/mne/evoked` | Evoked response(s) in MNE format (ave.fif), one per condition when by_event_type is true. |
| `out_dir_report` | `report/html` | HTML report (report.html) with the evoked response visualisations. |

<details>
<summary><b>Parameters</b> (3)</summary>

| Parameter | Type | Default | Description |
|---|---|---|---|
| `picks` | string |  | The channel type to plot. For 'grad', the gradiometers are collected in pairs and the RMS for each pair is plotted. If None the first available channel type from order shown above is used. Defaults to None. |
| `method` | string | `mean` | How to combine epochs: 'mean' or 'median' (passed to Epochs.average). |
| `by_event_type` | boolean | `true` | If true, one Evoked object is computed per event type (condition); if false, all epochs are averaged together. |

</details>

<!-- brainlife-app:end -->

## Running the App

### On brainlife.io

Open the App at [doi.org/10.25663/brainlife.app.618](https://doi.org/10.25663/brainlife.app.618), choose `neuro/meeg/mne/epochs` from your project, set the parameters and press **Execute**. The results are saved to your project as `neuro/meeg/mne/evoked`, `report/html`.

### Locally

You need [Singularity/Apptainer](https://apptainer.org/) (the App runs in `brainlifemeeg/mne:1.12.1`), [`jq`](https://jqlang.github.io/jq/).

1. Clone this repository.
2. Create `config.json` with the paths to your inputs and the parameters:

   ```json
   {
       "fif": "/path/to/fif/fif",
       "picks": "",
       "method": "mean",
       "by_event_type": true
   }
   ```

3. Run `./main`.

## Configuration Parameters

| key | type | default | description |
|---|---|---|---|
| `picks` | string | `""` | Channels to average, passed to `mne.Epochs.average()`: a channel *type* (e.g. `"eeg"`, `"meg"`), specific channel names, `"all"`, or `"data"`. If `None`, all data channels are used. |
| `method` | string | `"mean"` | How to combine the data across epochs: `"mean"`/`"median"`, or any other value is passed through as a callable method name. |
| `by_event_type` | boolean | `true` | When `true`, epochs are grouped by event type and a separate `Evoked` object is returned for each condition. When `false`, all epochs are averaged together into a single `Evoked` object. |

## Local Testing

```bash
# Update config.json with your data path
# Then run:
python main.py
```

## Technical Details

- Built with MNE-Python
- Headless plotting via the matplotlib Agg backend
- Compatible with downstream Brainlife.io MNE apps

## Citing

If you use this App, please cite it, the software it builds on and brainlife.io:

- Compute evoked. brainlife.io App. [doi:10.25663/brainlife.app.618](https://doi.org/10.25663/brainlife.app.618)
- Gramfort A. et al. MEG and EEG data analysis with MNE-Python. Frontiers in Neuroscience 7:267 (2013). [doi:10.3389/fnins.2013.00267](https://doi.org/10.3389/fnins.2013.00267)
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. *Scientific Data* 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## Authors

- Saeed Zahran (https://github.com/zahransa)
- Maximilien Chaumon (https://github.com/dnacombo)

## Funding

[![Wellcome-226486/Z/22/Z](https://img.shields.io/badge/Wellcome-226486%2FZ%2F22%2FZ-purple.svg)](https://wellcome.org/)
[![NIH-NINDS-U24NS140384](https://img.shields.io/badge/NIH_NINDS-U24NS140384-green.svg)](https://reporter.nih.gov/project-details/11261037)
[![NIH-NINDS-UM1NS132207](https://img.shields.io/badge/NIH_NINDS-UM1NS132207-green.svg)](https://reporter.nih.gov/project-details/11411328)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://reporter.nih.gov/project-details/10262925)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://reporter.nih.gov/project-details/10428625)
[![NIH-NIMH-R01MH126699](https://img.shields.io/badge/NIH_NIMH-R01MH126699-green.svg)](https://reporter.nih.gov/project-details/10460628)
[![NIH-NIDCD-R01DC020088](https://img.shields.io/badge/NIH_NIDCD-R01DC020088-green.svg)](https://reporter.nih.gov/project-details/11140284)
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-2203524](https://img.shields.io/badge/NSF_BCS-2203524-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2203524)
[![NSF-IIS-1636893](https://img.shields.io/badge/NSF_IIS-1636893-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-OAC-2148729](https://img.shields.io/badge/NSF_OAC-2148729-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148729)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NSF-IIS-2148700](https://img.shields.io/badge/NSF_IIS-2148700-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148700)
[![NSF-OAC-1916518](https://img.shields.io/badge/NSF_OAC-1916518-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1916518)

<sub>brainlife.io, which runs this App, is publicly funded by Wellcome, the U.S. National Institutes of Health and the U.S. National Science Foundation; acknowledging that support helps keep it running.</sub>

## License

See [LICENSE](LICENSE).
