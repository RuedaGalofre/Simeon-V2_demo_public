# SIMEON: Local Livestock Data and Lightweight Agroclimatic ML Platform

**Applicant organization:** RUEDA GALOFRE E HIJOS S.A.S. - GIINTAG Research Group, Barranquilla, Atlantico, Colombia  
**Official ScienTI / Minciencias R&D group record:** https://scienti.colciencias.gov.co/gruplac/jsp/visualiza/visualizagr.jsp?nro=00000000020083

## Project overview

SIMEON is a local-first farm data management and decision-support platform designed in Colombia for smallholder cattle farmers and agricultural technicians in dry-tropic ecosystems. It helps organize farm observations, pasture checks, soil observations, weather logs, and field notes into traceable records for human review.

The wider SIMEON architecture uses Python services, FastAPI, SQLAlchemy, and PostgreSQL deployments. This public repository intentionally contains only a standalone, reproducible demonstration component. It does not expose the proprietary application, production database, customer records, credentials, or operational integrations.

## Public demonstration scope

This is a reduced public demonstration, not a full SIMEON release. No pre-trained or production model is included in this repository, and no model artifact is downloaded, saved, or exposed. The standalone script fits a temporary IsolationForest in memory from the included synthetic CSV each time it runs; the result exists only for that demonstration run.

## Human-scale AI approach

The demonstration combines deterministic data-validation guardrails with CPU-friendly statistical machine learning in Python and scikit-learn. A temporary IsolationForest identifies observations that are unusual relative to a small synthetic sample. A flag is a request for human field verification; it is not a diagnosis, a forecast, or an automated management instruction.

The validation schema also blocks biomass or forage-tonnage estimates when a physical field clipping measurement is absent. Original field records and derived analysis outputs are treated as separate data objects.

## Repository contents

- `open-schema-and-ml/` - JSON validation schema, synthetic sample data, and a runnable local anomaly-detection demo.
- `screenshots/` - anonymized views of the current Spanish local interface, with English filenames and captions in the user guide.
- `sample-reports/` - English technical and farmer-oriented PDF reports for the same synthetic demonstration analysis.
- `user-manual/` - English user guide that explains the Spanish interface and its end-to-end workflow.

All records in this repository are synthetic demonstration data. The published assets do not contain personal data, exact coordinates, customer information, production credentials, or a production database.

## Visual documentation

The current SIMEON interface is shown in Spanish because it is designed for its local users. The accompanying documentation is in English:

- [English user guide](user-manual/SIMEON_V2_User_Guide_EN.pdf) - illustrated explanation of the full interface workflow.
- [Technical report sample](sample-reports/Technical_Report_Sample.pdf) - English technical interpretation for the synthetic demonstration case.
- [Farmer field guide sample](sample-reports/Farmer_Field_Guide_Sample.pdf) - English plain-language companion report for the same `analysis_id`.

## Run the standalone ML demo

```bash
cd open-schema-and-ml
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python pasture_anomaly_demo.py
```

The script checks the schema-relevant columns, fits a small local IsolationForest model, prints the statistical threshold, and identifies the synthetic records that merit a field review. It needs no network connection or external service.

## Scope and license

The MIT License in this repository applies only to the public demonstration materials here: the validation schema, synthetic data, standalone demo code, screenshots, and sample reports. It does not grant rights to SIMEON's pre-existing proprietary platform or to any non-public dataset.

## Responsible use
## video 
https://youtu.be/PHp_wH1dvxU
This demonstration supports record review and discussion with farmers and technicians. It does not diagnose animal or crop health, prescribe treatments, calculate ##biomass without a physical measurement, or replace field verification.
