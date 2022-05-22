#! /usr/bin/env bash

# default postgres db port
POSTGRES_DB_PORT=5432

# Let the DB start
echo "Waiting for database on ${POSTGRES_DB_SERVER}:${POSTGRES_DB_PORT}... "

while ! nc -z "$POSTGRES_DB_SERVER" "$POSTGRES_DB_PORT"; do
  sleep 0.1
done

echo "PostgreSQL is ready to accept connection..."


