USERNAME=postgres
ACCOUNT_NAME= is24-object
S3_PATH=s3://${ACCOUNT_NAME}-datawario-artifacts/is24-addressable-objects/
ENVIRONMENT=dev
TIMESHIFT=0

docker:
	docker compose up -d

project-down:
	docker compose down
	rm -Rf postgres-data

connect-to-db:
	cp "./initial_data/GlobalLandTemperaturesByCity.csv" "./postgres-data/GlobalLandTemperaturesByCity.csv"
	docker exec -it planetly-case_postgres_1 psql -U postgres -d postgres


