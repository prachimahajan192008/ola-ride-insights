"""Step 5: Streamlit app.  Run:  streamlit run app.py
pip install streamlit pandas sqlalchemy pymysql plotly
Reads ola_clean.csv by default (works anywhere, incl. Streamlit Cloud).
Set USE_MYSQL = True to run the SQL on your MySQL database instead.
"""
import sqlite3
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Ola Ride Insights", layout="wide")
st.title("🚖 Ola Ride Insights")

USE_MYSQL = False

@st.cache_resource
def get_conn():
    if USE_MYSQL:
        from sqlalchemy import create_engine
        return create_engine("mysql+pymysql://root:YOUR_PASSWORD@localhost:3306/ola")
    con = sqlite3.connect(":memory:", check_same_thread=False)
    pd.read_csv("ola_clean.csv").to_sql("ola_bookings", con, index=False)
    return con

QUERIES = {
 "1. Successful bookings": "SELECT * FROM ola_bookings WHERE Booking_Status='Success' LIMIT 1000",
 "2. Avg distance per vehicle type": "SELECT Vehicle_Type, ROUND(AVG(Ride_Distance),2) AS Avg_Distance FROM ola_bookings WHERE Booking_Status='Success' GROUP BY Vehicle_Type",
 "3. Cancelled by customers": "SELECT COUNT(*) AS Cancelled_By_Customer FROM ola_bookings WHERE Booking_Status='Canceled by Customer'",
 "4. Top 5 customers by rides": "SELECT Customer_ID, COUNT(*) AS Total_Rides FROM ola_bookings GROUP BY Customer_ID ORDER BY Total_Rides DESC, Customer_ID LIMIT 5",
 "5. Driver cancels: personal & car issues": "SELECT COUNT(*) AS Cancelled FROM ola_bookings WHERE Canceled_Rides_by_Driver='Personal & Car related issue'",
 "6. Prime Sedan max/min driver rating": "SELECT MAX(Driver_Ratings) AS Max_Rating, MIN(Driver_Ratings) AS Min_Rating FROM ola_bookings WHERE Vehicle_Type='Prime Sedan'",
 "7. UPI rides": "SELECT * FROM ola_bookings WHERE Payment_Method='UPI' LIMIT 1000",
 "8. Avg customer rating per vehicle": "SELECT Vehicle_Type, ROUND(AVG(Customer_Rating),2) AS Avg_Rating FROM ola_bookings GROUP BY Vehicle_Type",
 "9. Total value of successful rides": "SELECT SUM(Booking_Value) AS Total_Booking_Value FROM ola_bookings WHERE Booking_Status='Success'",
 "10. Incomplete rides + reason": "SELECT Booking_ID, Vehicle_Type, Incomplete_Rides_Reason FROM ola_bookings WHERE Incomplete_Rides='Yes'",
}

tab1, tab2, tab3 = st.tabs(["📊 SQL Insights", "🔎 Explore data", "📈 Power BI dashboard"])

with tab1:
    choice = st.selectbox("Pick a question", list(QUERIES))
    st.code(QUERIES[choice], language="sql")
    res = pd.read_sql(QUERIES[choice], get_conn())
    st.dataframe(res, use_container_width=True)

with tab2:
    df = pd.read_sql("SELECT * FROM ola_bookings", get_conn())
    c1, c2, c3 = st.columns(3)
    veh = c1.multiselect("Vehicle type", sorted(df.Vehicle_Type.unique()))
    sta = c2.multiselect("Booking status", sorted(df.Booking_Status.unique()))
    pay = c3.multiselect("Payment method", sorted(df.Payment_Method.dropna().unique()))
    q = st.text_input("Search Booking ID / Customer ID")
    if veh: df = df[df.Vehicle_Type.isin(veh)]
    if sta: df = df[df.Booking_Status.isin(sta)]
    if pay: df = df[df.Payment_Method.isin(pay)]
    if q: df = df[df.Booking_ID.str.contains(q, case=False) | df.Customer_ID.str.contains(q, case=False)]
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Bookings", f"{len(df):,}")
    k2.metric("Success rate", f"{(df.Booking_Status.eq('Success').mean()*100 if len(df) else 0):.1f}%")
    k3.metric("Revenue (success)", f"₹{df.loc[df.Booking_Status=='Success','Booking_Value'].sum():,.0f}")
    k4.metric("Avg driver rating", f"{df.Driver_Ratings.mean():.2f}")
    st.plotly_chart(px.histogram(df, x="Hour", color="Booking_Status", title="Bookings by hour"), use_container_width=True)
    st.dataframe(df.head(500), use_container_width=True)

with tab3:
    st.write("Publish your report in Power BI Service → File → Embed report → Publish to web, paste the URL below.")
    url = st.text_input("Power BI embed URL")
    if url:
        st.components.v1.iframe(url, height=600)
