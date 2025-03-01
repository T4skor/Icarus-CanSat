#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BMP280.h>
#include <Adafruit_HMC5883_U.h>

void setup() {
    Serial.begin(9600);
    while (!Serial);

    setupBMP280();
    setupHMC5883L();
    Serial.println("✅ Sensores inicializados correctamente.");
}

void loop() {
    leerBMP280();
    leerHMC5883L();
    delay(1000);
}
