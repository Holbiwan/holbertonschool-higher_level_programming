-- Creates a database hbtn_0d_usa
-- Creates a table cities in this database hbtn_0d_usa
-- State_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table
-- Description name=VARCHAR(256) can’t be null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    id INT UNIQUE AUTO_INCREMENT NOT NULL,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);