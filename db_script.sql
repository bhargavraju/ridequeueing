DROP DATABASE IF EXISTS app_db;
CREATE DATABASE IF NOT EXISTS app_db;
USE app_db;
CREATE TABLE requests (
    request_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    driver_id INT DEFAULT NULL,
    customer_id INT NOT NULL,
    request_time DATETIME NOT NULL DEFAULT now(),
    picked_up DATETIME DEFAULT NULL,
    completed DATETIME DEFAULT NULL
    );