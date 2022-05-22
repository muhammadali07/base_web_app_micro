#!/bin/bash
set -e

echo "If encounter error, please delete the keycloack-db container then delete postgres_data volume"
# CREATE TABLE AND USER FOR API-DB
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER $POSTGRES_DB_API_USER WITH ENCRYPTED PASSWORD '$POSTGRES_DB_API_PASSWORD';
    CREATE DATABASE $POSTGRES_DB_API;
    GRANT ALL PRIVILEGES ON DATABASE $POSTGRES_DB_API TO $POSTGRES_DB_API_USER;
EOSQL

echo "Finished init new table with its auth for API database."

