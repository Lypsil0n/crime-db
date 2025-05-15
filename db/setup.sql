DROP ROLE IF EXISTS dbadm;

DROP TABLE IF EXISTS mal;

DROP PROCEDURE IF EXISTS add_record;

CREATE ROLE dbadm LOGIN PASSWORD 'dbadm';
ALTER ROLE dbadm WITH SUPERUSER;

CREATE TABLE mal
(
    malnummer VARCHAR(20) NOT NULL,
    tilltalad VARCHAR(255) NOT NULL,
    personnummer VARCHAR(13) NOT NULL,
    brottsrubricering VARCHAR(255) NOT NULL,
    datum VARCHAR(255) NOT NULL,
    lank VARCHAR(255)
);

\i 'db/insert.sql'