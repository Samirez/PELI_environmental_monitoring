import time
import numpy as np
import paho.mqtt.client as mqtt
import time

def getTemp_RH():
   return t,h

def fire_detected(node_id):
    return("Suspicion of fire detected.(Node id)")

client = mqtt.Client()
#client.connect("192.168.1.108",1883)
#client.subscribe("/node/+/temperature-humidity")

def on_mqtt_message(client, data, message,temp=False,humidity=False):
  global t
  global h
  node = int(message.topic.split("/")[2])
  temp, hum = message.payload.decode("utf-8").split(",")
  t, h = float(temp), float(hum)
  #print(f"node: {node}, temp: {temp}, hum: {hum}, time: {time.time()}")
  if(temp and humidity):
      return t,h
  elif(temp):
      return t
  elif(humidity):
      return h
  

#client.on_message = on_mqtt_message
#client.loop_start()




''' 
#V1
while(True):
        currentTemp , currentRH = getTemp_RH()  #RH = relative humidity
        Temp, RH = [],[]
        if currentTemp > 40:
            if currentRH < 28:
                i = 1
                Temp[0],RH[0] = currentTemp, currentRH
                while(i<10):
                    Temp[i],RH[i] = getTemp_RH()
                    time.sleep(10)
                    i+=1
                if(np.mean(Temp[5:]) >= np.mean(Temp[0:5]) and np.mean(RH[5:])>= np.mean[0:5]):
                    fire_detected()
                else:
                    i=0
        else:
            print("Aucune détection")
'''

"" 
#V2

i = 0
t = 0
n = 12
T, H = [],[]
T_threshold, H_threshold = 40, 28

while(True):
    while(i<n):
        #getting temperature values from sensors through mqtt client
        T.append(on_mqtt_message(client,data,message,temp=True))
        H.append(on_mqtt_message(client,data,message,humidity=True))

        

        time.sleep(t)
        i+=1
    
    #evaluating
    if(np.mean(T) < T_threshold and np.mean(H) > H_threshold):
        T, H = [],[]
        i = 0
    
    else:
        fire_detected()
        T, H = [],[]
        i = 0
        


        

    




####

'''
###
# Pseudo code based on the paper : 
###


i = 0
n = 100 #depends on sampling period
P = 5 # period
WT = []
T_threshold = 45
while(True):
    T,H = getTemp_RH()
    if(i<=n):
        WT[i] = T
        i+=1
    else:
        omega =  T/np.mean(WT)
        while(omega>T_threshold):
            T,H = getTemp_RH()
            #send informmation
            #...
            #...
            #...
            t = t+P
            omega = T/np.mean(WT)
            t = 0
            i = 0
'''

    


        
                
            



