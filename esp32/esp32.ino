#include <Wire.h>

#include <SparkFun_Qwiic_Humidity_AHT20.h>
AHT20 humiditySensor;

void setup() {
  Serial.begin(115200);
  Serial.println("Qwiic Humidity AHT20 examples");

  Wire.begin(2, 3);

  if (humiditySensor.begin() == false) {
    Serial.println("AHT20 not detected. Please check wiring. Freezing.");
    while (1);
  }
  Serial.println("AHT20 acknowledged.");
}

void loop()
{
  if (humiditySensor.available() == true) {
    float temperature = humiditySensor.getTemperature();
    float humidity = humiditySensor.getHumidity();

    Serial.print("Temperature: ");
    Serial.print(temperature, 2);
    Serial.print(" C\t");
    Serial.print("Humidity: ");
    Serial.print(humidity, 2);
    Serial.print("% RH");

    Serial.println();
  }

  delay(2000);
}
