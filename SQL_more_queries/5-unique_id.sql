-- Creates a table unique_id on MySQL server.
-- The database name will be passed as an argument of the mysql command.
-- If the table unique_id already exists, the script should not fail.
CREATE TABLE IF NOT EXISTS unique_id(id INT DEFAULT 1 UNIQUE, name VARCHAR(256));