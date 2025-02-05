CREATE DATABASE mouse_events;
USE mouse_events;

CREATE TABLE events (
    id INT AUTO_INCREMENT PRIMARY KEY,
    event_type VARCHAR(50),
    x INT,
    y INT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
