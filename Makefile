connect-to-db:
	docker exec -it postgres psql -U postgres -d postgres

setup-environment:
	pip3 install virtualenv==20.0.15
	virtualenv env
	source env/bin/activate; \
	pip3 install -r requirements.txt

format:
	@echo Formatting...
	source env/bin/activate; \
	python -m black application/

lint: format
	@echo Linting...
	source env/bin/activate; \
	python -m flake8 application/