CREATE TABLE temperatures_by_time_and_city  (
    date date,
    avg_temperature NUMERIC,
    avg_temperature_uncertainty NUMERIC,
    city TEXT,
    country TEXT,
    latitude TEXT,
    longitude TEXT,
    PRIMARY KEY (dt, City, Country, Latitude, Longitude)
    );
 

