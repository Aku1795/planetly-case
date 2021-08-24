import json
import os
import datetime as dt

from flask import request, Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import desc

# app
app = Flask(__name__)

# DB connection
user = os.environ["POSTGRES_USER"]
password = os.environ["POSTGRES_PASSWORD"]
host = os.environ["POSTGRES_HOST"]
database = os.environ["POSTGRES_DB"]
port = os.environ["POSTGRES_PORT"]

DATABASE_CONNECTION_URI = (
    f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI


db = SQLAlchemy(app)

# DB models
Base = automap_base()
Base.prepare(db.engine, reflect=True)
TemperaturesByCity = Base.classes.temperatures_by_time_and_city


# Routes
@app.route("/")
def index():
    return "Hello world"


@app.route("/add_city", methods=["POST"])
def add_city():

    data = request.get_json()
    date = dt.datetime.strptime(data["date"], "%Y-%m-%d")
    avg_temperature = data["avg_temperature"]
    avg_temperature_uncertainty = data["avg_temperature_uncertainty"]
    city = data["city"]
    country = data["country"]
    latitude = data["latitude"]
    longitude = data["longitude"]

    new_city = TemperaturesByCity(
        date=date,
        avg_temperature=avg_temperature,
        avg_temperature_uncertainty=avg_temperature_uncertainty,
        city=city,
        country=country,
        latitude=latitude,
        longitude=longitude,
    )
    db.session.add(new_city)
    db.session.commit()

    return f"{city} added"


@app.route("/modify_city", methods=["POST"])
def modify_city():

    data = request.get_json()
    date = dt.datetime.strptime(data["date"], "%Y-%m-%d")
    avg_temperature = data.get("avg_temperature")
    avg_temperature_uncertainty = data.get("avg_temperature_uncertainty")
    city = data["city"]
    country = data["country"]

    query = (
        db.session.query(TemperaturesByCity)
        .filter(TemperaturesByCity.date == date)
        .filter(TemperaturesByCity.city == city)
        .filter(TemperaturesByCity.country == country)
    )

    if avg_temperature is not None:
        query.update({TemperaturesByCity.avg_temperature: avg_temperature})

    if avg_temperature_uncertainty is not None:
        query.update(
            {
                TemperaturesByCity.avg_temperature_uncertainty: avg_temperature_uncertainty
            }
        )

    db.session.commit()

    return f"{city} modified"


@app.route("/fetch_top_cities", methods=["POST"])
def fetch_top_cities():

    data = request.get_json()
    print(data)
    n_rows = data["n_rows"]
    start_date = data["start_date"]
    end_date = data["end_date"]

    query = (
        db.session.query(TemperaturesByCity)
        .filter(TemperaturesByCity.avg_temperature != None)
        .filter(TemperaturesByCity.date >= start_date)
        .filter(TemperaturesByCity.date <= end_date)
        .order_by(desc(TemperaturesByCity.avg_temperature))
        .limit(int(n_rows))
        .all()
    )

    results = []
    for result in query:
        new_row = {
            "date": result.date.strftime("%Y-%m-%d"),
            "avg_temperature": str(result.avg_temperature),
            "avg_temperature_uncertainty": str(result.avg_temperature_uncertainty),
            "city": result.city,
            "country": result.country,
            "latitude": result.latitude,
            "longitude": result.longitude,
        }
        results.append(new_row)

    return json.dumps(results)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
