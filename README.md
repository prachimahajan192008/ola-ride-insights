# Ola Ride Insights

Analysis of 1,03,024 Ola ride bookings (July 2024) using Python, SQL, Power BI and Streamlit.

## Problem statement
Ride-hailing platforms generate large amounts of booking data, but turning it into decisions is hard. This project cleans Ola's booking data and extracts insights on demand, cancellations, revenue and ratings.

## Tools used
Python (Pandas), SQL, Power BI, Streamlit, GitHub

## Project files
| File | Purpose |
|---|---|
| 01_clean_data.py | Cleans the data and adds Hour, Day and Week columns |
| ola_clean.csv | Cleaned dataset |
| 02_sql_queries.sql | 10 SQL queries (bookings, cancellations, ratings, revenue) |
| SQL_results.xlsx | Output of every SQL query |
| 03_load_to_mysql.py | Loads the data into MySQL |
| OLA_dashboard.pbix | Power BI dashboard (5 pages) |
| app.py | Streamlit web app |

## Approach
1. **Data cleaning:** converted the text "null" values into real blanks, fixed data types, checked for duplicate bookings (none), and created Hour, Day and Week features.
2. **SQL:** wrote 10 queries on bookings, distance, cancellations, ratings and payments.
3. **Power BI:** built a 5-page dashboard: Overall, Vehicle Type, Revenue, Cancellation, Ratings.
4. **Streamlit:** built an app that runs the SQL queries, filters the data and shows the dashboard.

## Key findings
- 62% of bookings succeed; driver cancellations (18%) are almost double customer cancellations (10%).
- Demand peaks at 8am, 12pm and 3pm, and is highest Monday to Wednesday.
- Cash brings in the most revenue (₹1.93 crore), followed by UPI (₹1.42 crore).
- Success rate, ratings (about 4.0) and distance are almost identical across vehicle types, so no vehicle type clearly stands out.
- Top cancellation reasons: drivers not moving to the pickup point (customers) and personal or car issues (drivers).

## Business suggestions
- Add drivers at peak hours (8am, 12pm, 3pm) and on Mondays to Wednesdays.
- Reduce driver cancellations with incentives and vehicle checks.
- Encourage UPI payment to cut cash handling.

## Live app
[(https://ola-ride-insights-01.streamlit.app/)]

## Dashboard Screenshots
[<img width="832" height="624" alt="1_ride_volume" src="https://github.com/user-attachments/assets/a7c4aa48-2642-408c-88f6-2fb52eed9dcd" />
<img width="832" height="624" alt="3_top_vehicle_distance" src="https://github.com/user-attachments/assets/91b22d5f-d891-4c90-8018-12f9f61c88ff" />
<img width="832" height="624" alt="6_revenue_payment" src="https://github.com/user-attachments/assets/6107f7fa-5cbb-4068-a8d1-bf61c4c79632" />
<img width="832" height="624" alt="7_top_customers" src="https://github.com/user-attachments/assets/3f797ad5-73c9-4a9b-b1fd-1141794e6b4e" />
<img width="832" height="624" alt="8_distance_day" src="https://github.com/user-attachments/assets/e3e30ad0-00f7-40af-bc95-81acab8f779a" />]


## How to run locally
pip install -r requirements.txt
streamlit run app.py
