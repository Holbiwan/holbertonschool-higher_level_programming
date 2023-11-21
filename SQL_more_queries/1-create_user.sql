-- Creates a new user_0d_1.
-- Password is set to 'user_0d_1_pwd'
-- Grant all privileges to user_0d_1
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
