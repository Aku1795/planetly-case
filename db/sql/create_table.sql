CREATE TABLE temperatures_by_time_and_city  (
    date date,
    avg_temperature NUMERIC,
    avg_temperature_uncertainty NUMERIC,
    city TEXT,
    country TEXT,
    latitude TEXT,
    longitude TEXT,
    PRIMARY KEY (date, City, Country, Latitude, Longitude)
    );
 

curl -XPOST -H "Content-type: application/json" -d \
{"n_rows": 1, "start_date": "2000-01-01", "end_date": "2030-01-01"} \
'localhost:5000/fetch_top_cities'