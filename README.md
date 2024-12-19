# QuakeQueryAPI

## Getting Started

To start the database, run the following command:

```
docker-compose up
```

This will create the database and initialize the database from the CSV file into the quakedb.earthquake_data table.

The first time it initializes will take roughly a minute.  After that it should be available.

The pgadmin tool can be found at http://localhost:15432

The user info for the pgadmin tool is in the docker-compose.yml file.
The user info for the database is in the .env file.

That should be all you need to get started.

## Build-out exercises
[ ] Pull a single record by ID and return as JSON from the python API.
[ ] Pull a list of earthquakes by date range and return as JSON from the python API.
[ ] Pull a list of earthquakes by magnitude range and return as JSON from the python API.

more to come...

## Happy Coding!