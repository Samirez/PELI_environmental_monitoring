import time
import numpy as np
import paho.mqtt.client as mqtt
import time

def connect_to_node(node):   
    client = mqtt.Client()
    client.connect("192.168.1.108",1883)
    client.subscribe("/"+node+"/+/temperature-humidity")
    client.loop_forever()

def on_mqtt_message(client, data, message):
  node = int(message.topic.split("/")[2])
  temp, hum = message.payload.decode("utf-8").split(",")
  temp, hum = float(temp), float(hum)
  print(f"node: {node}, temp: {temp}, hum: {hum}, time: {time.time()}")
  return temp,hum

def get_temp_humidity():
   t,h = on_mqtt_message
   return t,h

def fire_detected(node_id):
    return("Suspicion of fire detected",node_id)


#V1
def fire_detectV1(node):
    connect_to_node(node)
    while(True):
            currentTemp , currentRH = get_temp_humidity()  #RH = relative humidity
            Temp, RH = [],[]
            if currentTemp > 40:
                if currentRH < 28:
                    i = 1
                    Temp[0],RH[0] = currentTemp, currentRH
                    while(i<10):
                        Temp[i],RH[i] = get_temp_humidity()
                        time.sleep(10)
                        i+=1
                    if(np.mean(Temp[5:]) >= np.mean(Temp[0:5]) and np.mean(RH[5:])>= np.mean[0:5]):
                        fire_detected(node)
                    else:
                        i=0
            else:
                print("Nothing detected")
        
#V2
def fire_detectv2(node):
    connect_to_node(node)
    time = 5 
    n = 12
    T, H = [],[]
    T_threshold, H_threshold = 40, 28

    while(True):
        i = 0
        while(i<n):
            #getting values from sensors through mqtt client every 5 seconds
            temp , humidity = get_temp_humidity()
            T.append(temp)
            H.append(humidity)
            time.sleep(time)
            i+=1
        
        #evaluating
        if(np.mean(T) < T_threshold and np.mean(H) > H_threshold):
            T, H = [],[]
            i = 0   
        else:
            fire_detected(node)
            T, H = [],[]
            i = 0