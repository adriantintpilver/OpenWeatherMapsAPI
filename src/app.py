import sqlite3
from accessdata import sql_querys 

from functions import store_forecast_data, high_temperatures, average_temperatures

locations = ["London", "Paris", "New York", "Tokyo", "Sydney", "Rio de Janeiro", "Mumbai", "Shanghai", "Moscow", "Cape Town"]

#high temperatures a month
store_forecast_data(locations)
high_temperatures()
conn = sqlite3.connect('weather_data.db')
cursor = conn.execute(sql_querys['query_weather_forecast_high_temperatures'])
print("highest temperature: " + str(cursor.fetchall()))

#average temperatures a day
average_temperatures()
conn = sqlite3.connect('weather_data.db')
cursor = conn.execute(sql_querys['query_weather_forecast_average_temperatures'])
print("average temperature: " + str(cursor.fetchall()))

conn.close()