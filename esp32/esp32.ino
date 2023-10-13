#include "Arduino.h"
#include <Wire.h>
#include <SparkFun_Qwiic_Humidity_AHT20.h>
#include "painlessMesh.h"
#include "secrets.h"

#define   MESH_PORT       5555

AHT20 humiditySensor;
Scheduler userScheduler; // to control your personal task
painlessMesh mesh;

#define FORWARDER 3859401677

void sendMessage() ; // Prototype so PlatformIO doesn't complain

Task taskSendMessage( TASK_SECOND * 1 , TASK_FOREVER, &sendMessage );

void sendMessage() {
  if (humiditySensor.available() == true) {
    float temperature = humiditySensor.getTemperature();
    float humidity = humiditySensor.getHumidity();
    String msg = "";
    msg += temperature;
    msg += ",";
    msg += humidity;
    if (mesh.getNodeId() != FORWARDER) {
      Serial.println(msg);
      Serial.print("Sending message to ");
      Serial.println(FORWARDER);
      mesh.sendSingle(FORWARDER, msg);
    } else {
      Serial.print(mesh.getNodeId());
      Serial.print(",");
      Serial.println(msg);
    }
  }

  taskSendMessage.setInterval( random( TASK_SECOND * 1, TASK_SECOND * 5 ));
}

void receivedCallback( uint32_t from, String &msg ) {
  Serial.printf("%u,%s\n", from, msg.c_str());
}

void newConnectionCallback(uint32_t nodeId) {
    Serial.printf("log:New Connection, nodeId = %u\n", nodeId);
}

void changedConnectionCallback() {
  Serial.printf("log:Changed connections\n");
}

void nodeTimeAdjustedCallback(int32_t offset) {
    Serial.printf("log:Adjusted time %u. Offset = %d\n", mesh.getNodeTime(),offset);
}

void setup() {
  Serial.begin(115200);
  Wire.begin(2, 3);

  if (humiditySensor.begin() == false) {
    Serial.println("log:AHT20 not detected. Please check wiring. Freezing.");
    while (1);
  }

  //mesh.setDebugMsgTypes( ERROR | MESH_STATUS | CONNECTION | SYNC | COMMUNICATION | GENERAL | MSG_TYPES | REMOTE ); // all types on
  mesh.setDebugMsgTypes( ERROR | STARTUP );  // set before init() so that you can see startup messages

  mesh.init( MESH_PREFIX, MESH_PASSWORD, &userScheduler, MESH_PORT );
  mesh.onReceive(&receivedCallback);
  mesh.onNewConnection(&newConnectionCallback);
  mesh.onChangedConnections(&changedConnectionCallback);
  mesh.onNodeTimeAdjusted(&nodeTimeAdjustedCallback);

  Serial.print("log:Node id: ");
  Serial.println(mesh.getNodeId());

  userScheduler.addTask( taskSendMessage );
  taskSendMessage.enable();
}

void loop()
{
  mesh.update();
}


// white cable: 3859401677
// black cable: 3859403313
// red black cable: 3859403769
