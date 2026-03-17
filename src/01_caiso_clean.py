# src/01_caiso_clean.py

import pandas as pd
from pathlib import Path

RAW_PATH   = Path("data/raw/public_queue_report.xlsx")
CLEAN_PATH = Path("data/clean/caiso_projects.parquet")

print("Loading raw Excel file...")
df = pd.read_excel(RAW_PATH, header=3)
print(f"  Raw shape: {df.shape}")

COLUMN_RENAMES = {
    "Project Name":                                          "project_name",
    "Queue Position":                                        "queue_position",
    "Interconnection Request\nReceive Date":                 "request_receive_date",
    "Queue Date":                                            "queue_date",
    "Application Status":                                    "application_status",
    "Study\nProcess":                                        "study_process",
    "Type-1":                                                "technology_type_1",
    "Type-2":                                                "technology_type_2",
    "Type-3":                                                "technology_type_3",
    "Fuel-1":                                                "fuel_type_1",
    "Fuel-2":                                                "fuel_type_2",
    "Fuel-3":                                                "fuel_type_3",
    "MW-1":                                                  "mw_1",
    "MW-2":                                                  "mw_2",
    "MW-3":                                                  "mw_3",
    "Net MWs to Grid":                                       "capacity_mw",
    "Full Capacity, Partial or Energy Only (FC/P/EO)":       "deliverability_status",
    "TPD Allocation Percentage":                             "tpd_allocation_pct",
    "Off-Peak Deliverability and Economic Only":             "off_peak_deliverability",
    "TPD Allocation Group":                                  "tpd_allocation_group",
    "County":                                                "county",
    "State":                                                 "state",
    "Utility":                                               "utility",
    "PTO Study Region":                                      "pto_study_region",
    "Station or Transmission Line":                          "point_of_interconnection",
    "Proposed\nOn-line Date\n(as filed with IR)":            "proposed_online_date",
    "Current\nOn-line Date":                                 "current_online_date",
    "Suspension Status":                                     "suspension_status",
    "Feasibility Study or Supplemental Review":              "feasibility_study",
    "System Impact Study or \nPhase I Cluster Study":        "system_impact_study",
    "Facilities Study (FAS) or \nPhase II Cluster Study":    "facilities_study",
    "Optional Study\n(OS)":                                  "optional_study",
    "Interconnection Agreement \nStatus":                    "interconnection_agreement_status",
}

df = df.rename(columns=COLUMN_RENAMES)
print(f"  Columns renamed: {len(COLUMN_RENAMES)}")

df["capacity_mw"] = pd.to_numeric(df["capacity_mw"], errors="coerce")
df["queue_position"] = df["queue_position"].astype(str)

for date_col in ["request_receive_date", "queue_date",
                 "proposed_online_date", "current_online_date"]:
    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")

print("  Data types converted.")

before = len(df)
df = df[df["project_name"].notna()]
after = len(df)
print(f"  Removed {before - after} non-project rows. Kept {after} projects.")

df["iso"] = "CAISO"

CLEAN_PATH.parent.mkdir(parents=True, exist_ok=True)
df.to_parquet(CLEAN_PATH, engine="pyarrow", index=False)

print(f"\n✅ Clean dataset saved to: {CLEAN_PATH}")
print(f"   Final shape: {df.shape}")
print(f"\nColumns in clean dataset:")
for col in df.columns:
    print(f"   {col}")
