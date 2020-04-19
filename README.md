# Todoapp

A simple CRUD Todo app :)

Mostly just a playground for building database backed apps.

## Requirements

* `make deps` in a fresh Conda env.
* A postgresSQL server. On linux/mac `apt-get install postgresql` See Initializing a Postgres server.
* run `createdb todoapp` from the command line to create the database for this app.
* `make run`

## Development

* run `make dev-deps`
* Set up database migrations folder using `flask db init`.


## Migrations

* Make a version of current data models with migration script in `migrations/versions/` use `flask db migrate`
* To upgrade database to current version in migration folder `flask db upgrade`
* To rollback a version: `flask db downgrade`

_Initializing a Postgres server: From the `Postgres.app`, hit"Initialize" button. Follow the instructions on the Postgres.app homepage to configure and initialize the postgres server_.
