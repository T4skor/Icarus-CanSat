#include <Adafruit_BMP280.h>

Adafruit_BMP280 bmp;

void setupBMP280() {
    if (!bmp.begin(0x76)) {
        Serial.println("Error: No se encontró el sensor BMP280.");
        while (1);
    }
    bmp.setSampling(Adafruit_BMP280::MODE_NORMAL,
                    Adafruit_BMP280::SAMPLING_X2,
                    Adafruit_BMP280::SAMPLING_X16,
                    Adafruit_BMP280::FILTER_X16,
                    Adafruit_BMP280::STANDBY_MS_500);
}

void leerBMP280() {
    float temperatura = bmp.readTemperature();
    float presion = bmp.readPressure() / 100.0F;  // en hPa
    float presionAtm = presion / 1013.25;  // convertir a atm
    float altitud = bmp.readAltitude(1013.25);

    Serial.print("Icarus: Temperatura: "); Serial.print(temperatura); Serial.print(" °C, ");
    Serial.print("Presión: "); Serial.print(presionAtm); Serial.print(" atm, ");
    Serial.print("Altitud: "); Serial.print(altitud); Serial.println(" m");
}

