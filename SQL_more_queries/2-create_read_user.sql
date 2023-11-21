-- Creates a database 'hbtn_0d_2
-- Creates an user 'user_0d_2'
-- Password is set to 'user_0d_2_pwd'
-- Grant select to user_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';