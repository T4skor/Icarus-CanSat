import serial
import datetime

class MagnetometerDataVisualizer:
    def __init__(self, puerto, baudios=9600):
        self.serial_port = serial.Serial(puerto, baudios, timeout=1)
        self.tiempo = []
        self.x = []
        self.y = []
        self.z = []
        self.tiempo_inicio = datetime.datetime.now()

    def obtener_datos_sensor(self):
        if self.serial_port.in_waiting > 0:
            try:
                linea = self.serial_port.readline().decode('utf-8').strip()
                print(f"Datos recibidos: {linea}")  # Para depuración
                if "X:" in linea and "Y:" in linea and "Z:" in linea:
                    # Parseo de los datos X, Y, Z
                    datos = linea.split(" ")
                    x_value = float(datos[1])
                    y_value = float(datos[3])
                    z_value = float(datos[5])

                    return x_value, y_value, z_value
            except Exception as e:
                print(f"Error al leer datos del sensor: {e}")
        return None, None, None

    def actualizar_datos(self):
        x, y, z = self.obtener_datos_sensor()
        if x is not None and y is not None and z is not None:
            # Calcula el tiempo transcurrido
            tiempo_actual = (datetime.datetime.now() - self.tiempo_inicio).total_seconds()
            self.tiempo.append(tiempo_actual)
            self.x.append(x)
            self.y.append(y)
            self.z.append(z)

    def obtener_datos(self):
        return self.tiempo, self.x, self.y, self.z
