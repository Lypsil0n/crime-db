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
    lank VARCHAR(255)
);

CREATE PROCEDURE add_record(
    malnummer VARCHAR(20),
    tilltalad VARCHAR(255),
    personnummer VARCHAR(13),
    brottsrubricering VARCHAR(255),
    lank VARCHAR(255)
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO mal (malnummer, tilltalad, personnummer, brottsrubricering, lank)
    VALUES (malnummer, tilltalad, personnummer, brottsrubricering, lank);
END;
$$;

\i 'db/insert.sql'