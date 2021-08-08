CREATE TABLE test  (
    dt date,
    AverageTemperature NUMERIC,
    AverageTemperatureUncertainty NUMERIC,
    City TEXT,
    Country TEXT,
    Latitude TEXT,
    Longitude TEXT,
    PRIMARY KEY (dt, City, Country)
    );
 
--COPY test FROM '/var/lib/postgresql/data/GlobalLandTemperaturesByCity.csv' CSV HEADER;

