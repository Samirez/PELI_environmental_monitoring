CREATE TABLE IF NOT EXISTS sensors (
    Node_id INTEGER PRIMARY KEY AUTOINCREMENT,
    Latitude NUMERIC(8, 6),
    Longitude NUMERIC(9, 6)
);

CREATE TABLE IF NOT EXISTS sensorReadings (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    node_id INT,
    Temperature float NOT NULL,
    Humidity float NOT NULL,
    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (node_id) REFERENCES sensors(Node_id)
);