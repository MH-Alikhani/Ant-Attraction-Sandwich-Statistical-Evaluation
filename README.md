

# Ant Attraction to Sandwich Types – Statistical Analysis

## Overview

This repository contains the full code and data used for the statistical analysis presented in the report titled  
**“Ant Attraction to Sandwich Types: A Statistical Evaluation”**, submitted as part of the application process for the **Master of Science in Data Science** program at **TU Dortmund University** (Winter Semester 2025).

The analysis investigates how various sandwich attributes—including type of bread, topping, and the presence or absence of butter—affect the number of ants attracted to each variant. The project employs exploratory data analysis, ANOVA, post hoc comparisons, and Poisson regression to derive statistically valid conclusions from a fully factorial experimental design.

---

## Repository Structure

```

📁 datasets/             → CSV files containing the raw experimental data
📁 src/sandwich\_problem/ → Python scripts for data loading, visualization, and analysis
📁 results/              → Output figures, tables, and model summaries
📁 tests/                → Unit tests for verifying analytical functions
📄 pyproject.toml        → Poetry configuration for environment management
📄 README.md             → Project overview and instructions (this file)

````

---

## Requirements

This project uses [Poetry](https://python-poetry.org/) to manage dependencies. To install all necessary packages, run:

```bash
poetry install
````

Alternatively, using `pip`:

```bash
pip install -r requirements.txt
```

The project relies on the following core libraries:

* `pandas`, `numpy` – data handling
* `matplotlib`, `seaborn` – visualization
* `statsmodels`, `scipy`, `pingouin` – statistical testing
* `pytest` – testing framework

---

## Full Report

The complete academic report based on this code and analysis is available [here](https://github.com/MH-Alikhani/Ant-Attraction-to-Sandwich-Types---Statistical-Analysis/blob/main/report.pdf). It adheres to the standards of the TU Dortmund Data Science program and includes background, methodology, evaluation, and discussion.

---

## Academic Integrity

All analysis code has been written by the applicant. No part of the code or report was generated using AI tools unless explicitly noted. The statistical approach is original, reproducible, and aligns with academic standards as outlined in the application guide for TU Dortmund.

---

## References

* Montgomery, D. C. (2017). *Design and Analysis of Experiments*. Wiley.
* Kutner, M. H., Nachtsheim, C. J., & Neter, J. (2005). *Applied Linear Statistical Models*. McGraw-Hill Education.
* Field, A. (2013). *Discovering Statistics Using Python*. Sage Publications.
* Python packages: `seaborn`, `statsmodels`, `pingouin`, `scipy`, `pandas` – cited in the report bibliography.

---

## Contact

📧 For questions regarding this analysis or the report, please contact:
\[mohammad.hosein.alikhani08@gmail.com]

---

**Note**: This repository is made publicly available to ensure transparency and reproducibility of the presented results, in compliance with the TU Dortmund application requirements.
