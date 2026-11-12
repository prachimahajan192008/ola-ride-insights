"""Step 1: load raw OLA July sheet, clean it, save ola_clean.csv + ola.db (SQLite for testing)."""
import sys
import pandas as pd

RAW = sys.argv[1]            # path to OLA_DataSet.xlsx
df = pd.read_excel(RAW, sheet_name="July", usecols=range(19))   # drops the Vehicle Images column

# 1. The file stores missing values as the TEXT 'null' -> convert to real NaN
df = df.replace("null", pd.NA)

# 2. Fix types
df["Date"] = pd.to_datetime(df["Date"]).dt.date
df["Time"] = df["Time"].astype(str)
for c in ["V_TAT", "C_TAT", "Driver_Ratings", "Customer_Rating"]:
    df[c] = pd.to_numeric(df[c], errors="coerce")

# 3. Derived features for the dashboard
dt = pd.to_datetime(df["Date"].astype(str) + " " + df["Time"])
df["Hour"] = dt.dt.hour
df["Day_Name"] = dt.dt.day_name()
df["Week"] = dt.dt.isocalendar().week.astype(int)
df["Is_Success"] = (df["Booking_Status"] == "Success").astype(int)

# 4. Quality checks
assert df["Booking_ID"].is_unique, "duplicate booking IDs"
print("rows:", len(df))
print(df.isna().sum())

df.to_csv("ola_clean.csv", index=False)
print("saved ola_clean.csv")
