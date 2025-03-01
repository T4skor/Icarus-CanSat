import serial
import datetime

class SensorDataVisualizer:
    def __init__(self, puerto, baudios=9600):
        self.serial_port = serial.Serial(puerto, baudios, timeout=1)
        self.tiempo = []
        self.altitud = []
        self.temperatura = []
        self.altitud_actual = 0.0
        self.temperatura_actual = 0.0
        self.tiempo_inicio = datetime.datetime.now()

    def obtener_datos_sensor(self):
        if self.serial_port.in_waiting > 0:
            try:
                linea = self.serial_port.readline().decode('utf-8').strip()
                print(f"Datos recibidos: {linea}")  # Para depuración
                if "Icarus" in linea:
                    if "Temperatura" in linea:
                        self.temperatura_actual = float(linea.split(": ")[2].replace(" °C", ""))
                    elif "Altitud" in linea:
                        self.altitud_actual = float(linea.split(": ")[2].replace(" m", ""))
            except Exception as e:
                print(f"Error al leer datos del sensor: {e}")

    def actualizar_datos(self):
        self.obtener_datos_sensor()
        # Calcula el tiempo transcurrido
        tiempo_actual = (datetime.datetime.now() - self.tiempo_inicio).total_seconds()
        self.tiempo.append(tiempo_actual)
        self.altitud.append(self.altitud_actual)
        self.temperatura.append(self.temperatura_actual)

    def obtener_datos(self):
        return self.tiempo, self.altitud, self.temperatura
