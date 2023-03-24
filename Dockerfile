FROM python:3

RUN mkdir /openweathermap_api

WORKDIR /openweathermap_api

COPY requirements.txt /openweathermap_api

RUN pip install -r requirements.txt

COPY . /openweathermap_api

CMD [ "python", "src/app.py" ]