-- Prepare mysql server for this project
CREATE DATABASE IF NOT EXISTS movie_db;
CREATE USER IF NOT EXISTS 'abdul'@'localhost' IDENTIFIED BY 'aminah.aliyah';
GRANT ALL PRIVILEGES ON movie_db.* TO 'abdul'@'localhost';
GRANT SELECT ON performance_schema.* TO 'abdul'@'localhost';
FLUSH PRIVILEGES;