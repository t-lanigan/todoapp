APP_NAME := todoapp

deps:
	pip install -r requirements.txt

dev-deps:
	pip install -r requirements-dev.txt

run:
	FLASK_APP=app.py FLASK_DEBUG=true flask run

reset-db:
	dropdb $(APP_NAME) && createdb $(APP_NAME)
	flask db upgrade

start-db-server:
	pg_ctl -D /usr/local/var/postgres start

stop-db-server:
	pg_ctl -D /usr/local/var/postgres stop

connect-to-db:
	psql $(APP_NAME)

