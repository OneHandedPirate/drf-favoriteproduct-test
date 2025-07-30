create_dev_env:
	uv sync --no-group prod

create_dev_env_file:
	echo "DB__HOST='localhost'\nDB__PORT=5432\nDB__USER='postgres'\nDB__NAME='dev'\nDB__PASSWORD='postgres'" > .env

up_dev_db:
	 docker compose -f docker-compose-dev.yaml up -d

make_migrations:
	uv run manage.py migrate

load_dev_data:
	uv run manage.py loaddata db_dump/*

start_dev:
	uv run manage.py runserver

run_tests:
	uv run manage.py test
