# SIMEON: Local Livestock Data and Lightweight Agroclimatic ML Platform

**Applicant organization:** RUEDA GALOFRE E HIJOS S.A.S. - GIINTAG Research Group, Barranquilla, Atlántico, Colombia  
**Official ScienTI / Minciencias R&D group record:**  
https://scienti.colciencias.gov.co/gruplac/jsp/visualiza/visualizagr.jsp?nro=00000000020083

## Project overview

SIMEON V2.0 is a local-first farm data management and decision-support platform designed in Colombia for smallholder cattle farmers and agricultural technicians in dry-tropic ecosystems.

It helps organize pasture observations, soil observations, weather logs, and field notes into traceable records for human review.

The wider SIMEON architecture uses Python services, FastAPI, SQLAlchemy, and PostgreSQL deployments. This public repository intentionally contains only a standalone and reproducible demonstration component. It does not expose the proprietary application, production database, customer records, credentials, or operational integrations.

## Public demonstration scope

This repository is a reduced public demonstration, not a full SIMEON release. It contains synthetic demonstration data only.

No production model artifact, production database, customer record, credential, or operational integration is included in this repository. The local demonstration runs without external services and does not download or expose a production model.

## Nature-low local model

**Nature-low** is the intermediate identifier used for the local anomaly-detection model in SIMEON V2.0 Y SUELO.

It is implemented in Python with `scikit-learn` using `IsolationForest`. In this public demonstration, Nature-low is trained temporarily in memory from the included synthetic CSV every time the script runs.

Nature-low identifies pasture, rainfall, temperature, and soil-condition combinations that are statistically unusual relative to the synthetic demonstration sample. A flagged record requires human field verification; it is not a diagnosis, forecast, or automatic management instruction.

## Human-scale AI approach

The demonstration combines deterministic data-validation guardrails with CPU-friendly statistical machine learning in Python and scikit-learn.

Nature-low uses a temporary local `IsolationForest` to identify unusual observations in the synthetic sample. The result supports a conversation between the farmer and the technician before any management decision is made.

The validation schema also blocks biomass or forage-tonnage estimates when a physical field clipping measurement is unavailable. Original field records and derived analysis outputs are treated as separate data objects.

## Current scope and roadmap

SIMEON V2.0 Y SUELO is the official name of this project stage.

The public demonstration currently operates the pasture and soil module. During the next 12 months, SIMEON is planned to integrate four additional modules to complete the five modules proposed for the wider platform.

This repository demonstrates only the reproducible public component for pasture, soil, and local anomaly detection. It does not represent the complete future platform.

## Repository contents

- `open-schema-and-ml/` - JSON validation schema, synthetic sample data, and a runnable Nature-low local anomaly-detection demo.
- `screenshots/` - Anonymized views of the current Spanish local interface, with English filenames and captions in the user guide.
- `sample-reports/` - English technical and farmer-oriented PDF reports for the same synthetic demonstration analysis.
- `user-manual/` - English illustrated user guide that explains the Spanish interface and its end-to-end workflow.
- `USER_MANUAL.md` - Concise Markdown version of the user workflow.

All records in this repository are synthetic demonstration data. The published assets do not contain personal data, exact coordinates, customer information, production credentials, or a production database.

## Visual documentation

The current SIMEON V2.0  interface is shown in Spanish because it is designed for its local users. The accompanying public documentation is in English.

- [English user guide](user-manual/SIMEON_V2_User_Guide_EN.pdf)
- [Technical report sample](sample-reports/Technical_Report_Sample.pdf)
- [Farmer field guide sample](sample-reports/Farmer_Field_Guide_Sample.pdf)
- [Markdown user manual](USER_MANUAL.md)

## Run the Nature-low local demo

```bash
cd open-schema-and-ml
python -m venv .venv

# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
python pasture_anomaly_demo.py
```

The script validates the schema-relevant columns, trains Nature-low locally as an `IsolationForest`, prints the statistical threshold, and identifies synthetic records that merit field review.

It requires no network connection or external service.

## Demo video

Watch the SIMEON V2.0 · PASTURES AND SOIL demonstration here:

https://youtu.be/PHp_wH1dvxU 

## Responsible use

This demonstration supports record review and discussion with farmers and technicians. It does not diagnose animal, crop, pasture, or soil health; prescribe treatments; calculate biomass without a physical field measurement; or replace field verification.
