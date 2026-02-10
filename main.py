import socket
import json
import time
import math

UDP_IP = "0"   # listen on all interfaces
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print("Listening for GPS data...")

prev_speed = None
prev_time = None

while True:
    data, addr = sock.recvfrom(1024)
    gps = json.loads(data.decode())

    speed = gps["speed"]          # m/s (usually)
    t = gps["timestamp"]          # seconds

    acceleration = None
    if prev_speed is not None:
        dt = t - prev_time
        if dt > 0:
            acceleration = (speed - prev_speed) / dt

    print(f"Speed: {speed:.2f} m/s", end="")
    if acceleration is not None:
        print(f" | Accel: {acceleration:.2f} m/s²")
    else:
        print()

    prev_speed = speed
    prev_time = t
