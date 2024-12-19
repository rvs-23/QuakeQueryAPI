CREATE TABLE earthquake_data (
    id SERIAL PRIMARY KEY NOT NULL,
    epoch_time BIGINT,
    place TEXT,
    status TEXT,
    tsunami INT,
    significance INT,
    data_type TEXT,
    magnitude FLOAT,
    state TEXT,
    longitude FLOAT,
    latitude FLOAT,
    depth FLOAT,
    date_txt TEXT,
    timestamp TIMESTAMP
);

COPY earthquake_data(epoch_time, place, status, tsunami, significance, data_type, magnitude, state, longitude, latitude, depth, date_txt)
    FROM '/docker-entrypoint-initdb.d/Eartquakes-1990-2023.csv'
    DELIMITER ','
    CSV HEADER;

update earthquake_data set timestamp = to_timestamp(epoch_time / 1000);

alter TABLE earthquake_data drop COLUMN epoch_time;