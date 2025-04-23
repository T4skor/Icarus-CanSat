# Sensor Data Visualizer and Exporter via Serial Port

This Python script reads real-time data from a microcontroller (e.g., Arduino) via serial port, processes it, dynamically visualizes it using `matplotlib`, and exports it to Excel (`.xlsx`) files with embedded charts using `openpyxl`.

## 📦 Dependencies

Install the required libraries with:

```bash
pip install pyserial matplotlib pandas openpyxl
```

## 🔧 Configuration

Edit these lines according to your setup:

```python
port = 'COM6'       # Serial port connected to the microcontroller
baudrate = 9600     # Communication speed (must match the microcontroller)
```

## 📈 Supported Sensors

The script currently supports two types of sensor data:

- **BMP280**: Sends **Temperature**, **Pressure**, and **Altitude** data.
- **Magnetometer (e.g., HMC5883L)**: Sends **X**, **Y**, and **Z** magnetic field values in µT.

## 🎨 Features

- Real-time plots:
  - Temperature vs Time
  - Altitude vs Time
  - Magnetometer (X, Y, Z) vs Time
- Automatic saving of sensor data to `datos_sensores.xlsx`
- Creation of `datos_sensores_con_graficas.xlsx` with:
  - Full data table
  - Embedded charts (Temperature, Altitude, Magnetometer)

## 🧪 Expected Input Format (from Serial)

The script uses regular expressions to identify lines like:

```plaintext
Icarus: Temperature: 24.50 °C, Pressure: 1.02 atm, Altitude: 123.45 m
Icarus: X: 50.23 µT Icarus: Y: -12.34 µT Icarus: Z: 4.56
```

Ensure your Arduino (or similar device) sends data in this format.

## 📂 Output Files

- `datos_sensores.xlsx`: Raw data only
- `datos_sensores_con_graficas.xlsx`: Data + embedded charts

## 📝 Notes

- The script was tested on Windows. If you're on Linux, replace `'COM6'` with something like `'/dev/ttyUSB0'`.
- The time value used is a simple index (`i`) incremented on each update. Use `time.time()` for real timestamps if needed.

## 🧑‍💻 Author

Script developed by [T4skor]
