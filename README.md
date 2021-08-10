# Planetly data-engineering case

## Context

Planetly is a company specializing in evaluating the carbon footprint of companies using digital solutions. I applied for a data engineer role at this company and I got asked to setup a database based on a csv alongside an api to access the database. This repositery contains my work.

## How to launch the app

In order to launch the application and the db please make sure the csv containing the data can be found in the folder `./db/initial_data`.

When it is the case simply run the following command:

```bash 
docker compose up
```

Please wait roughly 4 min before making any call to the api (this waiting time is caused by the loading of the csv into the db)

## Design choices and possible improvement points

### DB

I hesitated between SQLite and Posgres for the database. I opted for Postgres because I was more familiar with the system.

There are a couple of things I could have done better:

- Preprocess the csv before loading it into the db - for instance converting the latitude and longitude fields into numeric fields.
- Put some indexes in place to improve performances during the api calls

### API

For the API I decided to use Flask as a webframework. The 2 main reasons for that choice are familiarity and not needing a complex framework given the relatively simple system.

One thing that I could have done better is modularise the different components of the API into different python packages (having `route.py` or `db.py` file for instance) and make use of some object oriented programming. At the moment the whole app resides in the app.py file.

I also could have used a `wait_for_it.sh` script in order to make the kick start of my two services smoother.

In total I would say that I spent 4 hours on the case. 

## API doc

Speaking about the API let us get into how it works. It has 3 main routes all of them POST methods:

- `/add_city`
- `/modifiy_city`
- `/fetch_top_cities`

#### add city

The body of the request must be of the following format:

```json
{"date": "2021-07-31"
,"avg_temperature": 39.26
,"avg_temperature_uncertainty": 0.37
,"city": "Ahvaz"
,"country": "Iran"
,"latitude": "31.35N"
,"longitude": "49.01E"}
```

It then adds a row to the unique table in the database.

#### Modifiy_city


```json
{"date": "2021-07-31"
,"avg_temperature": 39.26
,"avg_temperature_uncertainty": 0.37
,"city": "Ahvaz"
,"country": "Iran"}
```

It then modifies the entry given the city, country and date. Those 3 criterias cannot be empty, whereas avg_temperature and avg_temperature_uncertainty can.


#### fetch_top_cities

The body of the request must be of the following format:


```json
{"n_rows": 1, "start_date": "2000-01-01", "end_date": "2030-01-01"}
```

It then fetches the top n cities with the highest avg_temperature in the given time range.


## Examples

Here are the requests I made to my API to answer the questions in the instrations

*Question 1:*
```bash
curl -XPOST -H "Content-type: application/json" -d \
{"n_rows": 1, "start_date": "2000-01-01", "end_date": "2030-01-01"} \
'localhost:5000/localhost:5000/fetch_top_cities'
```
*Question 2:*

```bash
curl --location --request POST 'localhost:5000/add_city' \
--header 'Content-Type: application/json' \
--data-raw '{"date": "2021-07-31"
,"avg_temperature": 39.26
,"avg_temperature_uncertainty": 0.37
,"city": "Ahvaz"
,"country": "Iran"
,"latitude": "31.35N"
,"longitude": "49.01E"}'
```

*Question 3:*
```bash
curl --location --request POST 'localhost:5000/modify_city' \
--header 'Content-Type: application/json' \
--data-raw '{"date": "2021-07-31"
,"avg_temperature": 36.276
,"city": "Ahvaz"
,"country": "Iran"}'
```
