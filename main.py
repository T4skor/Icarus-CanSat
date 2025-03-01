import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
from primaria import SensorDataVisualizer
from secundaria import MagnetometerDataVisualizer

# Configuración de puertos
puerto = "COM7"  # Cambia este valor según corresponda

# Inicializa los visualizadores
visualizador_bmp = SensorDataVisualizer(puerto)
visualizador_magnetometro = MagnetometerDataVisualizer(puerto)

# Crear la figura de la gráfica
figura, ax = plt.subplots(figsize=(10, 8))

def actualizar_graficas(frame):
    # Actualizar los datos de ambos sensores
    visualizador_bmp.actualizar_datos()
    visualizador_magnetometro.actualizar_datos()

    # Obtener los datos actualizados
    tiempo_bmp, altitud, temperatura = visualizador_bmp.obtener_datos()
    tiempo_mag, x, y, z = visualizador_magnetometro.obtener_datos()

    # Limpiar la gráfica y agregar nuevas líneas
    ax.clear()
    ax.plot(tiempo_bmp, altitud, label="Altitud", color="blue")
    ax.plot(tiempo_bmp, temperatura, label="Temperatura", color="red")
    ax.plot(tiempo_mag, x, label="Magnetómetro X", color="green")
    ax.plot(tiempo_mag, y, label="Magnetómetro Y", color="orange")
    ax.plot(tiempo_mag, z, label="Magnetómetro Z", color="purple")

    # Configurar las etiquetas y el título
    ax.set_title("Datos del Sensor: Altitud, Temperatura y Magnetómetro")
    ax.set_xlabel("Tiempo (s)")
    ax.set_ylabel("Valor")
    ax.legend()

# Crear animación
anim = FuncAnimation(figura, actualizar_graficas, interval=1000)
plt.tight_layout()
plt.show()

# Guardar los datos en un archivo Excel después de la animación (esto puede ser después de cierto tiempo o cuando se detenga la animación)
def guardar_datos_excel():
    tiempo_bmp, altitud, temperatura = visualizador_bmp.obtener_datos()
    tiempo_mag, x, y, z = visualizador_magnetometro.obtener_datos()

    # Crear un DataFrame de pandas
    datos = {
        "Tiempo": tiempo_bmp,
        "Altitud": altitud,
        "Temperatura": temperatura,
        "Magnetómetro X": x,
        "Magnetómetro Y": y,
        "Magnetómetro Z": z
    }
    df = pd.DataFrame(datos)

    # Guardar en un archivo Excel
    df.to_excel("datos_sensor.xlsx", index=False)

# Llamar a guardar los datos en algún momento adecuado (puedes agregar esta función en un botón o detener la animación)
guardar_datos_excel()
