"""Step 2: load ola_clean.csv into MySQL (needed for Power BI + Streamlit).
Run once:  pip install pandas sqlalchemy pymysql
Edit the 3 variables below first. Create the DB in MySQL Workbench:  CREATE DATABASE ola;
"""
import pandas as pd
from sqlalchemy import create_engine

USER, PASSWORD, DB = "root", "YOUR_PASSWORD", "ola"
engine = create_engine(f"mysql+pymysql://{USER}:{PASSWORD}@localhost:3306/{DB}")

df = pd.read_csv("ola_clean.csv")
df.to_sql("ola_bookings", engine, if_exists="replace", index=False, chunksize=10000)
print("Loaded", len(df), "rows into", DB, ".ola_bookings")
