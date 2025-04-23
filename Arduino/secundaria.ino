#include <Wire.h>
#include <QMC5883LCompass.h>

QMC5883LCompass compass;

void iniciarMagnetometro() {
  // Inicializar el sensor
  compass.init();
}

void leerMagnetometro() {
  // Leer los valores del magnetómetro
  compass.read();

  // Obtener los valores de los ejes
  int x = compass.getX();
  int y = compass.getY();
  int z = compass.getZ();

  // Factor de conversión (escala para 8 Gauss)
  float scale = 0.0015;  // Escala para el rango de 8 Gauss

  // Convertir las lecturas a Gauss
  float xGauss = x * scale;
  float yGauss = y * scale;
  float zGauss = z * scale;

  // Convertir las lecturas a Microteslas (1 Gauss = 100 Microteslas)
  float xMicroteslas = xGauss * 100;
  float yMicroteslas = yGauss * 100;
  float zMicroteslas = zGauss * 100;

  // Mostrar los valores de los ejes en el monitor serie en Microteslas
  Serial.print("Icarus: X: ");
  Serial.print(xMicroteslas);
  Serial.print(" µT  Icarus: Y: ");
  Serial.print(yMicroteslas);
  Serial.print(" µT  Icarus: Z: ");
  Serial.println(zMicroteslas);

  delay(500); // Esperar medio segundo antes de la siguiente lectura
}
