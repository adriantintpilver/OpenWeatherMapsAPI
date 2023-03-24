import sqlite3
import requests
import json

from accessdata import sql_querys 
import config 

def get_forecast_data(location):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={config.api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
        return data
    else:
        return None

def store_forecast_data(locations):
    for location in locations:
        forecast_data = get_forecast_data(location)
        if forecast_data is not None:
            store_data(parse_data(location, forecast_data))

def parse_data(location, data):
    # Parse the data and return a list of dictionaries
    #data = json.loads(str(data))

    result_list = []

    for item in data['list']:
        date_time = item['dt_txt'] # extraer la fecha y hora
        temperature = item['main']['temp'] # extraer la temperatura del elemento
        result_list.append({'location': location, 'date': date_time, 'temperature': temperature})

    return result_list

def store_data(data_list):
    # Connect to the database
    conn = sqlite3.connect('weather_data.db')
    
    # Create the weather_forecast table if it doesn't exist
    conn.execute(sql_querys['create_weather_forecast'])
    
    # Deduplicate the data
    deduplicated_data = []
    for element in data_list:
        if element not in deduplicated_data:
            deduplicated_data.append(element)
    
    # Store the deduplicated data in the database
    for data in deduplicated_data:
        # Check if the data already exists in the database
        cursor = conn.execute(sql_querys['check_weather_forecast_exist'], (data['location'], data['date'], data['temperature']))
        existing_data = cursor.fetchone()
        if existing_data is None:
            # Insert the data into the database
            conn.execute(sql_querys['insert_weather_forecast'], (data['location'], data['date'], data['temperature']))
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def high_temperatures():
    # Connect to the database
    conn = sqlite3.connect('weather_data.db')
    # Create the weather_forecast_high_temperatures table if it doesn't exist
    conn.execute(sql_querys['create_weather_forecast_high_temperatures'])
    # Delete the weather_forecast_high_temperatures data
    conn.execute(sql_querys['delete_weather_forecast_high_temperatures'])
    # seek for the highest temperature of each month in each location
    conn.execute(sql_querys['insert_weather_forecast_high_temperatures'])
    conn.commit()
    conn.close()

def average_temperatures():
    # Connect to the database
    conn = sqlite3.connect('weather_data.db')
    # Create the weather_forecast_average_temperatures table if it doesn't exist
    conn.execute(sql_querys['create_weather_forecast_average_temperatures'])
    # Delete the weather_forecast_average_temperatures data
    conn.execute(sql_querys['delete_weather_forecast_average_temperatures'])
    # seek for the average temperature of each day in each location
    conn.execute(sql_querys['insert_weather_forecast_average_temperatures'])
    conn.commit()
    conn.close()