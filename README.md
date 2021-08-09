# planetly-case

##Examples

Question 1:
```bash
curl -XPOST -H "Content-type: application/json" -d \
{"n_rows": 1, "start_date": "2000-01-01", "end_date": "2030-01-01"} \
'localhost:5000/localhost:5000/fetch_top_cities'
```
Question 2:

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

Question 3:
```bash
curl --location --request POST 'localhost:5000/modify_city' \
--header 'Content-Type: application/json' \
--data-raw '{"date": "2021-07-31"
,"avg_temperature": 36.276
,"city": "Ahvaz"
,"country": "Iran"}'
```
