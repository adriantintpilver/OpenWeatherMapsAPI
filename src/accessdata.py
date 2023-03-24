sql_querys = {
    # Create the weather_forecast table if it doesn't exist
    'create_weather_forecast' : "CREATE TABLE IF NOT EXISTS weather_forecast (id INTEGER PRIMARY KEY AUTOINCREMENT, location TEXT NOT NULL, date TEXT NOT NULL, temperature REAL NOT NULL)",
    # Create the weather_forecast_high_temperatures table if it doesn't exist
    'create_weather_forecast_high_temperatures' : "CREATE TABLE IF NOT EXISTS weather_forecast_high_temperatures (id INTEGER PRIMARY KEY AUTOINCREMENT, location TEXT NOT NULL, month TEXT NOT NULL, year TEXT NOT NULL, date TEXT NOT NULL, temperature REAL NOT NULL)",
    # Create the weather_forecast_average_temperatures table if it doesn't exist
    'create_weather_forecast_average_temperatures' : "CREATE TABLE IF NOT EXISTS weather_forecast_average_temperatures (id INTEGER PRIMARY KEY AUTOINCREMENT, location TEXT NOT NULL, day TEXT NOT NULL, month TEXT NOT NULL, year TEXT NOT NULL, AVE_temperature REAL NOT NULL, MIN_temperature REAL NOT NULL, MAX_temperature REAL NOT NULL)",
    # Delete the weather_forecast_high_temperatures data
    'delete_weather_forecast_high_temperatures' : "DELETE FROM weather_forecast_high_temperatures;",
    # Delete the weather_forecast_average_temperatures data
    'delete_weather_forecast_average_temperatures' : "DELETE FROM weather_forecast_average_temperatures;",
    # Check if the data already exists in the database
    'check_weather_forecast_exist' : "SELECT id FROM weather_forecast WHERE location = ? AND date = ? AND temperature = ?",
    # insert data in weather_forecast
    'insert_weather_forecast' : "INSERT INTO weather_forecast (location, date, temperature) VALUES (?, ?, ?)",
    # insert data in weather_forecast_high_temperatures
    'insert_weather_forecast_high_temperatures' : "INSERT INTO weather_forecast_high_temperatures (location,month,year,date,temperature) SELECT location as location, strftime('%m', date) as month, strftime('%Y', date) as year, date as date, MAX(temperature) as temperature FROM weather_forecast GROUP BY location, strftime('%m', date), strftime('%Y', date) ORDER BY location, strftime('%m', date), strftime('%Y', date)",
    # insert data in weather_forecast_average_temperatures
    'insert_weather_forecast_average_temperatures' : "INSERT INTO weather_forecast_average_temperatures (location,day,month,year,AVE_temperature, MIN_temperature, MAX_temperature) SELECT location as location, strftime('%d', date) as day, strftime('%m', date) as month, strftime('%Y', date) as year, AVG(temperature) as AVE_temperature, MIN(temperature) as MIN_temperature, MAX(temperature) as MAX_temperature FROM weather_forecast GROUP BY location, strftime('%d', date), strftime('%m', date), strftime('%Y', date) ORDER BY location, strftime('%m', date), strftime('%Y', date)",
    # Select all data from weather_forecast_high_temperatures
    'query_weather_forecast_high_temperatures' : "SELECT * FROM weather_forecast_high_temperatures",
    # Select all data from weather_forecast_average_temperatures
    'query_weather_forecast_average_temperatures' : "SELECT * FROM weather_forecast_average_temperatures"
    }