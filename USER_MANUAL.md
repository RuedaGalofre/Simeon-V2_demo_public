# SIMEON V2 User Guide

## Purpose

SIMEON V2 is a local-first tool for documenting pasture and soil observations, reviewing stored records, identifying unusual combinations for human review, and exporting two traceable reports. The current interface is in Spanish; this guide explains each screen in English.

All screenshots use demonstration records. Names shown in the interface are demonstration labels and do not represent a production dataset.

## Public demonstration scope

This repository is a reduced public demonstration and does not include the complete SIMEON application, a production database, or any pre-trained or production model. The standalone demo fits a temporary IsolationForest in memory from synthetic data each time it runs. It does not download, save, or expose a model artifact.

## 1. Start with farms and field records

Open **Registro** (Registration). Add each farm once, then record a pasture observation and, when available, a soil observation for the same plot.

For the pasture form, record the plot, date, grass type, entry and exit height, and any available protein, temperature, humidity, rainfall, and field-note data. For the soil form, record texture, moisture, compaction, drainage, method, source, and observations.

Screens: `screenshots/01_dashboard_and_farms.png`, `screenshots/02_pasture_and_soil_forms.png`, and `screenshots/03_observation_fields.png`.

## 2. Review saved records

Open **Datos guardados** (Saved data). Filter by farm or search by plot to see stored pasture observations. Original field records remain separate from their later analysis outputs.

Screen: `screenshots/04_saved_records.png`.

## 3. Run a local review

Open **Análisis local** (Local analysis). Select a pasture observation and, if applicable, its associated soil observation. Select **Ejecutar análisis** (Run analysis).

SIMEON applies deterministic validation rules and, when available, a local statistical model. A flagged result indicates an unusual pattern for field verification. It is not a diagnosis, forecast, treatment recommendation, or automatic decision.

Screen: `screenshots/05_local_ml_analysis.png`.

## 4. Export reports

Open **Informes** (Reports). Each completed analysis receives an `analysis_id` that connects the technical report and the farmer-oriented field guide. Download both reports for the same analysis when sharing results.

Screen: `screenshots/06_traceable_reports.png`.

## Data-quality guardrail

SIMEON does not estimate biomass or forage tonnage when a physical field clipping measurement is unavailable. Confirm unusual records in the field and preserve the original measurement even when a later correction is recorded.
