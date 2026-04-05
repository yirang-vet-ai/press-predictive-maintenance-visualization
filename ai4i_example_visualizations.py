import pandas as pd
import matplotlib.pyplot as plt
import os

csv_path = "ai4i2020.csv"
df = pd.read_csv(csv_path)

df = df.rename(columns={
    "Air temperature [K]": "air_temp_k",
    "Process temperature [K]": "process_temp_k",
    "Rotational speed [rpm]": "rpm",
    "Torque [Nm]": "torque_nm",
    "Tool wear [min]": "tool_wear_min",
    "Machine failure": "machine_failure"
})

os.makedirs("outputs", exist_ok=True)

plt.rcParams.update({
    "figure.figsize": (10, 6),
    "font.size": 13,
    "axes.titlesize": 16,
    "axes.labelsize": 13,
    "xtick.labelsize": 11,
    "ytick.labelsize": 11,
    "legend.fontsize": 11
})

# 1) Machine failure count
plt.figure()
df["machine_failure"].value_counts().sort_index().plot(kind="bar")
plt.title("Machine Failure Count")
plt.xlabel("Machine Failure (0=Normal, 1=Failure)")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("outputs/01_machine_failure_count.png", dpi=180, bbox_inches="tight")
plt.close()

# 2) Tool wear by failure
plt.figure()
for label, subset in df.groupby("machine_failure"):
    subset["tool_wear_min"].plot(kind="hist", bins=30, alpha=0.5, label=f"Failure={label}")
plt.title("Tool Wear Distribution by Failure")
plt.xlabel("Tool Wear (min)")
plt.ylabel("Frequency")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/02_tool_wear_by_failure.png", dpi=180, bbox_inches="tight")
plt.close()

# 3) Torque by failure
plt.figure()
for label, subset in df.groupby("machine_failure"):
    subset["torque_nm"].plot(kind="hist", bins=30, alpha=0.5, label=f"Failure={label}")
plt.title("Torque Distribution by Failure")
plt.xlabel("Torque (Nm)")
plt.ylabel("Frequency")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/03_torque_by_failure.png", dpi=180, bbox_inches="tight")
plt.close()

# 4) Average sensor values
avg_df = df.groupby("machine_failure")[["air_temp_k", "process_temp_k", "rpm", "torque_nm", "tool_wear_min"]].mean().T
plt.figure(figsize=(11, 7))
avg_df.plot(kind="bar")
plt.title("Average Sensor Values: Normal vs Failure")
plt.xlabel("Feature")
plt.ylabel("Average Value")
plt.xticks(rotation=25, ha="right")
plt.tight_layout()
plt.savefig("outputs/04_avg_sensor_values_normal_vs_failure.png", dpi=180, bbox_inches="tight")
plt.close()

# 5) Failure type counts
failure_type_cols = ["TWF", "HDF", "PWF", "OSF", "RNF"]
failure_type_counts = df[failure_type_cols].sum().sort_values(ascending=False)
plt.figure()
failure_type_counts.plot(kind="bar")
plt.title("Failure Type Counts")
plt.xlabel("Failure Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("outputs/05_failure_type_counts.png", dpi=180, bbox_inches="tight")
plt.close()

print("Saved all charts in ./outputs")