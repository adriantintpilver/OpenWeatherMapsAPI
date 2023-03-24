## OpenWeatherMaps API

This is a dockerized python/sqlite API queries openweathermap.org and fetches a 5-day set of weather data for the locations we request (in app.py -> locations list) and returns:

```bash
A dataset containing the location, date and temperature of the highest temperatures reported by location and month.

A dataset containing the average temperature, min temperature, location of min temperature, and location of max temperature per day.
```

## Run in local

# without using docker
    You will need python installed and get a API_KEY from openweathermap.org and configure this credential in the .src/config.py file

#### For application run going to the root directory of the project run the following scripts

```bash
$ pip install -r requirements.txt
```
```bash
$ python src/app.py
```
# using docker
    You will need to have docker and docker compose installed.
        From the root directory of the project run the following scripts
        ```bash
        docker-compose up
        ```
in both cases need get a API_KEY from openweathermap.org and configure this credential in the .src/config.py file
You can also configure which world cities you want to consult in the "locations" list configured in the .src/app.py file, which right now has 10 example cities

```bash
locations = ["London", "Paris", "New York", "Tokyo", "Sydney", "Rio de Janeiro", "Mumbai", "Shanghai", "Moscow", "Cape Town"]
```
# Clarification on how this application runs 
This application runs once when called and returns the results in the console log, and must be called again if you want to call it again

For real use it would be necessary to include a query api service that receives the cities and returns the results, which can be easily added with flask but was not requested, so this is just an example.

## File structure
Inside the src folder, we find:

In functions.py we find the used to query the openweathermap.org api, create the tables, save the data in Sqlite, clean the data, get the required results and save these results in the database..

In the file accessdata.py we have all the sqlite db queries

In the config.py file, API_KEY for openweathermap.org is set



