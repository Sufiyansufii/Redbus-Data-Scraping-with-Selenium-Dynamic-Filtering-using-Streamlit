# Redbus-Data-Scraping-with-Selenium-Dynamic-Filtering-using-Streamlit
### Project Overview
This project aims to automate the extraction of bus travel data from the Redbus website and develop an interactive data filtering application using Streamlit. This project aims to provide real-time insights into bus routes, schedules, pricing, and seat availability. This can aid in understanding travel patterns, optimizing travel choices, and enhancing user experience. The project involves web scraping, data storage, and visualization to provide real-time insights and enhance user experience.

### Data Set

Source: Redbus website
Format: Structured data stored in a SQL database
Required Fields: Bus Route Link, Name, Type, Departure/Arrival Time, Rating, Price, Seats

### Task List

### Set Up Environment: Install required libraries and set up the project environment.
Programming:  Python, SQL Database 
Libraries Used: pandas, numpy, Selenium, Streamlit, sqlalchemy, datetime

#### Web Scraping with Selenium:
Automate browser actions to navigate and extract data from the Redbus website.
Extract relevant data fields such as route name, bus type, departure time, duration, arrival time, star rating, price, and seats available.

#### Data Storage:
The scraped data is structured and stored in a SQL database, which allows for efficient data management and retrieval. The database schema includes the following columns:
id (auto-incrementing primary key)
route_name (TEXT)
route_link (TEXT)
busname (TEXT)
bustype (TEXT)
departing_time (DATETIME)
duration (TEXT)
reaching_time (DATETIME)
star_rating (FLOAT)
price (DECIMAL)
seats_available (INT)

#### Data Cleaning and Preprocessing:
Clean the extracted data to remove inconsistencies and ensure accuracy.
Preprocess data for analysis and visualization.

#### Streamlit Application Development:
We developed an interactive web application using Streamlit that allows users to filter and visualize the data based on various parameters such as route, bus type, departure time, and price. The application provides a user-friendly interface for data exploration and analysis.

### Use Cases
Travel Aggregators: Provide real-time bus schedules, seat availability, and pricing information.
Market Analysis: Analyze travel patterns, preferences, and trends.
Customer Service: Improve user experience by offering personalized travel options based on historical data.

### Usage
Open the Streamlit application in your web browser.
Use the interactive filters to explore and analyze bus travel data.
Visualizations will update in real-time based on the selected filters.

### Future Enhancements

Real-Time Updates: Implementing real-time data updates to keep the information current.
Enhanced Filtering: Adding more filtering options and advanced search capabilities.

### Conclusion

This project demonstrates the successful application of web scraping, data storage, and interactive data visualization techniques to solve a real-world problem. The skills and methodologies developed in this project can be applied to various domains requiring automated data extraction and analysis.
