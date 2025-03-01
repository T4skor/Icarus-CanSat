#include <Adafruit_HMC5883_U.h>

Adafruit_HMC5883_Unified mag = Adafruit_HMC5883_Unified(12345);

void setupHMC5883L() {
    if (!mag.begin()) {
        Serial.println("⚠️ No se encontró el HMC5883L. Revisa las conexiones.");
        while (1);
    }
}

void leerHMC5883L() {
    sensors_event_t event;
    mag.getEvent(&event);

    Serial.print("Icarus: X: "); Serial.print(event.magnetic.x);
    Serial.print("Icarus: Y: "); Serial.print(event.magnetic.y);
    Serial.print("Icarus: Z: "); Serial.println(event.magnetic.z);
    Serial.println("----------------------------------");
}
