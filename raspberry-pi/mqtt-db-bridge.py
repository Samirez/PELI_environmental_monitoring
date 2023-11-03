#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import sqlite3
import time
import queue

db_con = sqlite3.connect("../db.sqlite3")
db = db_con.cursor()
q = queue.Queue()

def execute_sql_file(file, db):
  content = open(file, "r").read()
  commands = content.split(";")
  for command in commands:
    db.execute(command)

def on_mqtt_message(client, data, message):
  node = int(message.topic.split("/")[2])
  temp, hum = message.payload.decode("utf-8").split(",")
  temp, hum = float(temp), float(hum)
  print(f"node: {node}, temp: {temp}, hum: {hum}, time: {time.time()}")
  q.put((node, temp, hum))

client = mqtt.Client()
client.connect("localhost", 1883)

client.on_message = on_mqtt_message
client.subscribe("/node/+/temperature-humidity")

execute_sql_file("create_table.sql", db)
db_con.commit()
client.loop_start()

try:
    while True:
      node, temp, hum = q.get()
      db.execute("INSERT INTO sensorReadings (node_id_id, Temperature, Humidity) VALUES (?, ?, ?)", (node, temp, hum))
      db_con.commit()
except KeyboardInterrupt:
    pass

db_con.close()
client.disconnect()
