-- Creates database hbtn_0d_usa and the table states (in the database hbtn_0d_usa)
-- If the database hbtn_0d_usa already exists, the script should not fail.
-- If the table states already exists, the script should not fail.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY, name VARCHAR(256));