#!/usr/bin/env python3
import serial
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("localhost", 1883)

s = serial.Serial("/dev/ttyUSB0", 115200)

while True:
  line = s.readline().decode("utf-8").strip()
  print(line)
  if line.startswith("log:"):
    client.publish("/log", line.lstrip("log:"))
  else:
    if len(line.split(",")) != 3:
      continue
    node_id, temperature, humidity = line.split(",")
    client.publish(f"/node/{node_id}/temperature", temperature)
    client.publish(f"/node/{node_id}/humidity", humidity)
    client.publish(f"/node/{node_id}/temperature-humidity", f"{temperature},{humidity}")
  
client.disconnect()
