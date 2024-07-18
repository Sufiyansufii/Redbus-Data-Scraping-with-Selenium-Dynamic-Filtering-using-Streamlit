import mysql.connector
import pandas as pd
from datetime import datetime
import streamlit as st
import re

def get_data_from_db():
    # Connect to the database
    connection = mysql.connector.connect(
        host="localhost",
        user="your_user_name",
        password="your_password",
        database="redbus"
    )
    query = "SELECT * FROM bus_routes"
    df = pd.read_sql(query, connection)
    connection.close()
    return df

# Function to clean data (fill NaN values and convert types)
def clean_data(df):
    df['star_rating'] = df['star_rating'].fillna(0)
    df['price'] = df['price'].fillna(0)
    df['seats_available'] = df['seats_available'].fillna(df['seats_available'].median()).astype(int)
    return df

# Streamlit application
def main():
    st.title('Bus Route Information')

    # Get data from database
    df = get_data_from_db()

    # Clean data
    df = clean_data(df)

    # Sidebar filters
    st.sidebar.header('Filters')
    route_filter = st.sidebar.multiselect('Select Route', df['route_name'].unique())
    bus_type_filter = st.sidebar.multiselect('Select Bus Type', df['bustype'].unique())
    star_rating_filter = st.sidebar.slider('Select Star Rating', min_value=float(df['star_rating'].min()), max_value=float(df['star_rating'].max()), step=0.1)
    price_filter = st.sidebar.slider('Select Price Range', min_value=float(df['price'].min()), max_value=float(df['price'].max()), step=1.0)
    seats_available = st.sidebar.number_input("Seats Available", min_value=0, step=1)

    # Filter data based on user inputs
    filtered_data = df
    if route_filter:
        filtered_data = filtered_data[filtered_data['route_name'].isin(route_filter)]
    if bus_type_filter:
        filtered_data = filtered_data[filtered_data['bustype'].isin(bus_type_filter)]
    filtered_data = filtered_data[filtered_data['star_rating'] >= star_rating_filter]
    filtered_data = filtered_data[filtered_data['price'] <= price_filter]

    # Display filtered data
    st.write(filtered_data)

if __name__ == "__main__":
    main()