-- Tablespace: quakedb

-- DROP TABLESPACE quakedb;

CREATE TABLESPACE quakedb
  OWNER postgres
  LOCATION '/var/lib/postgresql/data';

ALTER TABLESPACE quakedb
  OWNER TO postgres;