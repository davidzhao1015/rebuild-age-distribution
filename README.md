# Building Onset Age Curves from Published Summary Statistics

This repository provides a practical workflow for estimating symptom onset age distributions of autoimmune disorders using data extracted from published literature.

Because individual patient data (IPD) are rarely available, the workflow focuses on working with summary statistics, like mean, median, IQR, quantiles, and min–max values, to reconstruct realistic distributions that can be used for further analysis or modeling.


## What This Project Does

- Reconstructs onset age distributions from different types of reported summary statistics.
- Deals with heterogeneous reporting formats (e.g., some studies report median/IQR, others only mean ± SD).
- Runs sensitivity analyses to understand how assumptions affect the results.
- Helps make study results more comparable and usable for downstream modeling.



## Repository Overview

This repo contains two main Jupyter notebooks

1. **01_construct_distribution.ipynb**
    
    Build onset age distributions from reported summary statistics.
    
    👉 [Read the related blog post](https://davidzhao1015.github.io/blog/2025/reconstruct-age-distribution/)
    
2. **02_sensitivity_analysis.ipynb**
    
    Explore how different assumptions and input ranges affect the reconstructed distributions.
    
<!--3. **03_fat_tail_optimization.ipynb**
    
    Fine-tune distribution parameters to better capture long tails in the data.-->
    

## Tools and Libraries

This project uses common Python packages:

- numpy
- pandas
- scipy
- matplotlib / seaborn
- jupyter

<!--Install everything with:

```
pip install -r requirements.txt
```-->

<!--## How to Run

1. **Clone this repository**:

```
git clone https://github.com/davidzhao1015/rebuild-age-distribution.git
cd <repo-name>
```

2. **Start Jupyter Lab or Notebook**:

```
jupyter lab
```
or

```
jupyter notebook
```

2. **Run the notebooks in order**:
    - 01_construct_distribution.ipynb
    - 02_sensitivity_analysis.ipynb
    <!--- 03_fat_tail_optimization.ipynb-->-->

## Tips & Notes

- The workflow is designed for summary-level data; no individual patient data required.
- You can easily adjust distribution assumptions (e.g., log-normal, gamma) inside the notebooks.
- Visual outputs are included to check the shape and fit of reconstructed distributions.
- Sensitivity analyses help you understand the range of plausible distributions.


<!--## ** License**

This project is released under the [MIT License](https://www.notion.so/LICENSE).-->


## Acknowledgment

This work builds on standard epidemiological and statistical practices for reconstructing distributions from published literature.
If you use or adapt this workflow in your own work, please cite or link back to this repository.
