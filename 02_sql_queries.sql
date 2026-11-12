-- OLA Ride Insights: 10 required SQL questions (table: ola_bookings)
-- Works in MySQL 8 and SQLite.

-- Q1. All successful bookings
CREATE VIEW IF NOT EXISTS Successful_Bookings AS
SELECT * FROM ola_bookings WHERE Booking_Status = 'Success';
SELECT * FROM Successful_Bookings;

-- Q2. Average ride distance per vehicle type
CREATE VIEW IF NOT EXISTS Avg_Distance_By_Vehicle AS
SELECT Vehicle_Type, ROUND(AVG(Ride_Distance),2) AS Avg_Distance
FROM ola_bookings WHERE Booking_Status = 'Success'
GROUP BY Vehicle_Type;
SELECT * FROM Avg_Distance_By_Vehicle;

-- Q3. Total rides cancelled by customers
CREATE VIEW IF NOT EXISTS Cancelled_By_Customer AS
SELECT COUNT(*) AS Total_Cancelled_By_Customer
FROM ola_bookings WHERE Booking_Status = 'Canceled by Customer';
SELECT * FROM Cancelled_By_Customer;

-- Q4. Top 5 customers by number of rides
CREATE VIEW IF NOT EXISTS Top_5_Customers AS
SELECT Customer_ID, COUNT(Booking_ID) AS Total_Rides
FROM ola_bookings GROUP BY Customer_ID
ORDER BY Total_Rides DESC, Customer_ID LIMIT 5;
SELECT * FROM Top_5_Customers;

-- Q5. Rides cancelled by drivers: personal & car related issues
CREATE VIEW IF NOT EXISTS Driver_Cancel_Personal_Car AS
SELECT COUNT(*) AS Driver_Cancelled_Personal_Car
FROM ola_bookings WHERE Canceled_Rides_by_Driver = 'Personal & Car related issue';
SELECT * FROM Driver_Cancel_Personal_Car;

-- Q6. Max and min driver ratings for Prime Sedan
CREATE VIEW IF NOT EXISTS Prime_Sedan_Driver_Ratings AS
SELECT MAX(Driver_Ratings) AS Max_Rating, MIN(Driver_Ratings) AS Min_Rating
FROM ola_bookings WHERE Vehicle_Type = 'Prime Sedan' AND Driver_Ratings IS NOT NULL;
SELECT * FROM Prime_Sedan_Driver_Ratings;

-- Q7. Rides paid by UPI
CREATE VIEW IF NOT EXISTS UPI_Payments AS
SELECT * FROM ola_bookings WHERE Payment_Method = 'UPI';
SELECT * FROM UPI_Payments;

-- Q8. Average customer rating per vehicle type
CREATE VIEW IF NOT EXISTS Avg_Customer_Rating AS
SELECT Vehicle_Type, ROUND(AVG(Customer_Rating),2) AS Avg_Customer_Rating
FROM ola_bookings WHERE Customer_Rating IS NOT NULL
GROUP BY Vehicle_Type;
SELECT * FROM Avg_Customer_Rating;

-- Q9. Total booking value of successful rides
CREATE VIEW IF NOT EXISTS Total_Successful_Value AS
SELECT SUM(Booking_Value) AS Total_Booking_Value
FROM ola_bookings WHERE Booking_Status = 'Success';
SELECT * FROM Total_Successful_Value;

-- Q10. Incomplete rides with reason
CREATE VIEW IF NOT EXISTS Incomplete_Rides_View AS
SELECT Booking_ID, Vehicle_Type, Incomplete_Rides_Reason
FROM ola_bookings WHERE Incomplete_Rides = 'Yes';
SELECT * FROM Incomplete_Rides_View;
