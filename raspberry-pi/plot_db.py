import sqlite3
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
query = "SELECT Temperature, Humidity, Timestamp, Node_id_id FROM sensorReadings"
cursor.execute(query)
rows = cursor.fetchall()
conn.close()

sensor_data = {}
for row in rows:
    temperature, humidity, timestamp, node_id = row
    if node_id not in sensor_data:
        sensor_data[node_id] = {'Temperature': [], 'Humidity': [], 'Timestamp': []}
    sensor_data[node_id]['Temperature'].append(temperature)
    sensor_data[node_id]['Humidity'].append(humidity)
    sensor_data[node_id]['Timestamp'].append(datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S"))

fig, axes = plt.subplots(2, 2, sharex=True, sharey=True, figsize=(10, 6))

def plot(id, title, row, col):
    data = sensor_data[id]
    if row == 0 and col == 0: # use the same label for all data
        axes[row][col].plot(data['Timestamp'], data['Temperature'], label='Temperature')
        axes[row][col].plot(data['Timestamp'], data['Humidity'], label='Humidity')
    else:
        axes[row][col].plot(data['Timestamp'], data['Temperature'])
        axes[row][col].plot(data['Timestamp'], data['Humidity'])
    axes[row][col].set_title(title)
    axes[row][col].xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    
plot(2365842813, "Indoor sensor 1", 0, 0)
plot(2365850613, "Indoor sensor 2", 0, 1)
plot(2365844053, "Outdoor sensor 1", 1, 0)
plot(403135765, "Outdoor sensor 2", 1, 1)

fig.legend()
plt.show()
