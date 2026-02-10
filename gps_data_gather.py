import serial

ser = serial.Serial(
    port="/dev/ttyUSB0",  # COM3 on Windows
    baudrate=9600,
    timeout=1
)

while True:
    line = ser.readline().decode(errors="ignore").strip()

    if line.startswith("$GPRMC"):
        parts = line.split(",")
        status = parts[2]

        if status == "A":  # A = active fix
            lat = parts[3]
            lat_dir = parts[4]
            lon = parts[5]
            lon_dir = parts[6]

            print(lat, lat_dir, lon, lon_dir)
