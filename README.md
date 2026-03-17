# energy-project-screening

# Energy Project Screening — CAISO Queue Analysis

A data analysis project exploring the California ISO (CAISO) interconnection 
queue to identify characteristics that correlate with stronger project 
deliverability outcomes.

## Project Overview

Before an energy project can connect to California's electrical grid, it must 
enter CAISO's interconnection queue and complete a series of engineering studies. 
This analysis examines 326 active queue projects to answer:

- What technologies dominate the queue?
- What drives Full Capacity deliverability status?
- Do hybrid projects (solar + storage) outperform standalone projects?
- Which regions produce the strongest deliverability outcomes?

## Key Findings

1. **Battery and solar dominate** — 90% of active queue projects are battery 
   storage or solar, reflecting California's clean energy policy priorities

2. **Battery achieves the highest Full Capacity rate** — ~80% of battery 
   projects receive Full Capacity deliverability, outperforming standalone 
   solar and wind (~50%)

3. **Storage reduces worst-case outcomes, not best-case outcomes** — Hybrid 
   projects cut Energy Only risk from 37% to 13%, but Full Capacity rates 
   are nearly identical to standalone projects (~52%)

4. **Geography is the dominant driver of Full Capacity deliverability** — 
   Metro LA and Northern California regions outperform Kern and Eastern 
   regions, suggesting transmission congestion is the binding constraint

## Project Structure
```
energy-project-screening/
│
├── data/
│   ├── raw/                          # Original CAISO Excel file (source of truth)
│   └── clean/                        # Processed Parquet dataset
│
├── src/
│   └── 01_caiso_clean.py             # Data cleaning pipeline
│
├── notebooks/
│   └── 02_caiso_analysis.ipynb       # Full analysis notebook
│
└── requirements.txt
```

## Pipeline
```
data/raw/public_queue_report.xlsx
        ↓
src/01_caiso_clean.py
        ↓
data/clean/caiso_projects.parquet
        ↓
notebooks/02_caiso_analysis.ipynb
```

The cleaning script and analysis notebook are intentionally separated. 
The cleaning script can be re-run anytime CAISO releases an updated Excel file.

## Setup
```bash
# Clone the repository
git clone <your-repo-url>
cd energy-project-screening

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the cleaning pipeline
python src/01_caiso_clean.py

# Open the analysis notebook
code notebooks/02_caiso_analysis.ipynb
```

## Requirements
```
pandas
pyarrow
fastparquet
matplotlib
openpyxl
```

## Data Source

CAISO Public Interconnection Queue Report  
California Independent System Operator (CAISO)  
https://www.caiso.com/planning/Pages/GeneratorInterconnection/Default.aspx

## About

Built as a portfolio project demonstrating:
- Data engineering: Excel → cleaning pipeline → Parquet
- Exploratory data analysis with pandas
- Portfolio-quality data visualization with matplotlib
- Energy industry domain knowledge