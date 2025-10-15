Meta-Analysis of Symptom Onset Age

This repository provides a practical workflow for estimating symptom onset age distributions of autoimmune disorders using data extracted from published literature.

Because individual patient data (IPD) are rarely available, the workflow focuses on working with summary statistics—like mean, median, IQR, quantiles, and min–max values—to reconstruct realistic distributions that can be used for further analysis or modeling.
⸻

What This Project Does
	•	Reconstructs onset age distributions from different types of reported summary statistics.
	•	Deals with heterogeneous reporting formats (e.g., some studies report median/IQR, others only mean ± SD).
	•	Runs sensitivity analyses to understand how assumptions affect the results.
	•	Optimizes parameters to better handle “fat tails” (e.g., rare late-onset cases).
	•	Helps make study results more comparable and usable for downstream modeling.
⸻

Repository Overview

This repo contains three main Jupyter notebooks:
	1.	`01_construct_distribution.ipynb`: Build onset age distributions from reported summary statistics.
👉 Read the related blog [post](https://davidzhao1015.github.io/blog/2025/reconstruct-age-distribution/)
	2.	`02_sensitivity_analysis.ipynb`: Explore how different assumptions and input ranges affect the reconstructed distributions.
	3.	`03_fat_tail_optimization.ipynb`: Fine-tune distribution parameters to better capture long tails in the data.
⸻

Tips & Notes
	•	The workflow is designed for summary-level data — no individual patient data required.
	•	You can easily adjust distribution assumptions (e.g., log-normal, gamma) inside the notebooks.
	•	Visual outputs are included to check the shape and fit of reconstructed distributions.
	•	Sensitivity analyses help you understand the range of plausible distributions.
⸻

Acknowledgment

This work builds on standard epidemiological and statistical practices for reconstructing distributions from published literature.

If you use or adapt this workflow in your own work, please cite or link back to this repository.


