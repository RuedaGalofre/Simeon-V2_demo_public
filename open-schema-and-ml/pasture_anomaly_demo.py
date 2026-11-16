"""Run a local, reproducible anomaly review on synthetic pasture data."""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import OrdinalEncoder


DATA_PATH = Path(__file__).with_name("synthetic_pasture_sample.csv")
FEATURE_COLUMNS = ["grass_height_cm", "rainfall_7d_mm", "air_temperature_c", "soil_condition"]
REQUIRED_COLUMNS = {
    "analysis_id", "record_uuid", "record_date", "record_type", "data_source",
    "measurement_method", "grass_height_cm", "soil_condition", "rainfall_7d_mm",
    "air_temperature_c", "physical_biomass_clipping_kg_m2", "synthetic_data_label",
}


def load_and_validate() -> pd.DataFrame:
    frame = pd.read_csv(DATA_PATH)
    missing = REQUIRED_COLUMNS - set(frame.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    if not 25 <= len(frame) <= 30:
        raise ValueError("The demonstration sample must contain 25 to 30 rows.")
    if not frame["synthetic_data_label"].eq("SYNTHETIC_DEMONSTRATION_DATA").all():
        raise ValueError("Only explicitly labelled synthetic demonstration data may be used.")
    if frame["analysis_id"].duplicated().any() or frame["record_uuid"].duplicated().any():
        raise ValueError("Traceability identifiers must be unique.")
    return frame


def feature_matrix(frame: pd.DataFrame) -> np.ndarray:
    encoder = OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=-1)
    soil = encoder.fit_transform(frame[["soil_condition"]])
    numeric = frame[["grass_height_cm", "rainfall_7d_mm", "air_temperature_c"]].to_numpy(dtype=float)
    return np.column_stack([numeric, soil])


def main() -> None:
    frame = load_and_validate()
    matrix = feature_matrix(frame)
    model = IsolationForest(n_estimators=150, contamination=0.14, random_state=42)
    model.fit(matrix)
    scores = model.score_samples(matrix)
    threshold = float(np.quantile(scores, 0.14))
    flagged = frame.assign(anomaly_score=scores).loc[scores <= threshold].copy()

    print("SIMEON local ML demonstration")
    print(f"Dataset: {len(frame)} synthetic pasture observations")
    print("Model: scikit-learn IsolationForest (150 estimators, random_state=42)")
    print(f"Statistical review threshold: anomaly score <= {threshold:.4f}")
    print(f"Flagged records for human field review: {len(flagged)}")
    print()
    for row in flagged.sort_values("anomaly_score").itertuples(index=False):
        biomass_status = "blocked: no physical field clipping" if pd.isna(row.physical_biomass_clipping_kg_m2) else "physical clipping recorded"
        print(
            f"{row.analysis_id} | {row.plot_label} | score={row.anomaly_score:.4f} | "
            f"height={row.grass_height_cm} cm | soil={row.soil_condition} | {biomass_status}"
        )
    print()
    print("Interpretation: flags identify unusual combinations in this synthetic sample.")
    print("They require field verification and do not diagnose pasture, soil, or animal health.")


if __name__ == "__main__":
    main()
