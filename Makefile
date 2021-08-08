USERNAME=postgres
ACCOUNT_NAME= is24-object
ENVIRONMENT=dev
TIMESHIFT=0
#cp "./initial_data/GlobalLandTemperaturesByCity.csv" "./postgres-data/GlobalLandTemperaturesByCity.csv"

docker:
	docker compose up -d

project-down:
	docker compose down
	rm -Rf postgres-data

connect-to-db:
	docker exec -it planetly-case_postgres_1 psql -U postgres -d postgres


