CREATE TABLE test  (
    dt date,
    AverageTemperature NUMERIC,
    AverageTemperatureUncertainty NUMERIC,
    City TEXT,
    Country TEXT,
    Latitude TEXT,
    Longitude TEXT,
    PRIMARY KEY (dt, City, Country, Latitude, Longitude)
    );
 

