#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BMP280.h>

void setup() {
    Serial.begin(9600);
    while (!Serial);
    iniciarMagnetometro();
    setupBMP280();
    Serial.println("✅ Sensores inicializados correctamente.");
}

void loop() {
    leerMagnetometro();
    leerBMP280();
    delay(500);
}
