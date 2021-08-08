USERNAME=postgres
ACCOUNT_NAME= is24-object
ENVIRONMENT=dev
TIMESHIFT=0

load-csv-into-db:
	docker exec --workdir=/repo planetly-case_postgres_1 psql --host=localhost --username=postgres --file=init_load.sql

project-up:
	docker compose up -d
	load-csv-into-db

project-down:
	docker compose down

connect-to-db:
	docker exec -it planetly-case_postgres_1 psql -U postgres -d postgres


