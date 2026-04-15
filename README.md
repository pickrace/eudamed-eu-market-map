# EU MedTech Readiness: Analyzing EUDAMED Before the May 2026 Deadline

This project analyzes EU medical device manufacturers' readiness for the mandatory EUDAMED rollout, effective 28 May 2026.

## Background

EUDAMED (European Database on Medical Devices) is the EU's centralized registry for medical devices, manufacturers, certificates, and market surveillance under the Medical Device Regulation (MDR 2017/745) and the In Vitro Diagnostic Regulation (IVDR 2017/746). On 26 November 2025, the European Commission declared the first four EUDAMED modules functional, triggering a six-month transition period. From **28 May 2026**, registration in EUDAMED becomes mandatory for all manufacturers placing devices on the EU market.

This creates a unique moment for analysis: the database is populated on a largely voluntary basis today, but will be the single source of truth within weeks. Mapping the current state reveals which countries, manufacturers, and device categories are ahead of the compliance curve — and where gaps remain.

## Research questions

1. How are registered medical device manufacturers distributed across EU member states?
2. Which device categories (by EMDN classification) dominate the registered dataset?
3. What share of registered manufacturers have also registered their devices — a proxy for compliance readiness?
4. How concentrated is the market? Which manufacturers and notified bodies hold the largest share of registrations?
5. What proportion of devices come from non-EU manufacturers operating through EU authorized representatives?

## Data source

Data is collected from the public [EUDAMED database](https://ec.europa.eu/tools/eudamed/) via its public JSON endpoints. The analysis focuses on the top-5 EU countries by registration volume (DE, FR, IT, NL, IE) to allow deeper country-level insight.

## Methodology

_To be documented in Session 2, once the scraper and data pipeline are complete._

## Key findings

_To be added after analysis is complete._

## Tech stack

- **Language:** Python 3.11
- **Data collection:** `requests`
- **Data processing:** `pandas`
- **Storage:** SQLite (planned, may change)
- **Visualization:** Power BI (planned, may change)

## Project structure

```
eudamed-eu-market-map/
├── data/
│   ├── raw/           # Raw JSON responses from EUDAMED API
│   └── processed/     # Cleaned CSVs ready for analysis
├── src/               # Python scripts (scraper, cleaner, loader)
├── notebooks/         # Jupyter notebooks for exploration
├── dashboard/
│   └── screenshots/   # Power BI dashboard exports
├── docs/              # Additional documentation
├── requirements.txt   # Python dependencies
└── README.md          # Info about project 
```

## How to run

_Full instructions coming in next commits._

```bash
# Clone the repository
git clone https://github.com/pickrace/eudamed-eu-market-map.git
cd eudamed-eu-market-map

# Create and activate a virtual environment
python -m venv venv
source venv/Scripts/activate  # On Windows Git Bash
# source venv/bin/activate    # On macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

## Project status

Big chunks of work in progress:

- [x] **Part 1:** Project setup, virtual environment, initial dependencies
- [ ] **Part 2:** EUDAMED API scraper for top-5 EU countries
- [ ] **Part 3:** Data cleaning, SQLite schema, loading pipeline
- [ ] **Part 4:** Power BI dashboard and final analysis

## Limitations

_To be documented alongside the final analysis. Known limitations already include: focus on top-5 EU countries (not pan-EU), snapshot analysis (no historical tracking), and reliance on voluntary pre-mandate registrations which may not reflect the full market._

## Author

**Maksym Pantia**  
[LinkedIn](https://www.linkedin.com/in/pickrace/) · [GitHub](https://github.com/pickrace)

## Acknowledgements
   
- Data provided by the European Commission via [EUDAMED](https://ec.europa.eu/tools/eudamed/).
- Development supported by AI as a teaching tool for code review, debugging, and documentation drafting.