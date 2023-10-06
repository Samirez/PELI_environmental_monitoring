CREATE TABLE sensor_readings {
node_id INT PRIMARY KEY,
temperature NUMERIC(10) not NULL,
humidity NUMERIC(10) not NULL,
time_stamp datetime
};
