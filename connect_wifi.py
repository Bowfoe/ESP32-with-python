from machine import Pin
import network
import socket
import sys
import time

# ------------------------
# Wi-Fi Configuration
# ------------------------
SSID = "OUR SSID"
PASSWORD = "OUR WIFI"

sta = network.WLAN(network.STA_IF)
sta.active(True)

if not sta.isconnected():
    print("Connecting to Wi-Fi...")
    sta.connect(SSID, PASSWORD)

    timeout = 10  # seconds
    start = time.ticks_ms()

    while not sta.isconnected():
        if time.ticks_diff(time.ticks_ms(), start) > timeout * 1000:
            print("Failed to connect to Wi-Fi.")
            sys.exit()

print("Connected to Wi-Fi!")
ip = sta.ifconfig()[0]
print("Device IP address:", ip)

# ------------------------
# TCP Server Configuration
# ------------------------
PORT = 8080

# Create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', PORT))  # Bind to all available interfaces
s.listen(5)         # Allow up to 5 pending connections

print("Server listening on port", PORT)

# ------------------------
# Accept a Single Client
# ------------------------
conn, addr = s.accept()
print("Client connected from:", addr)

# Receive data (up to 1024 bytes)
data = conn.recv(1024)
print("Received from client:", data)

# Send response
conn.send(b"Hello from ESP32!")

# Close connection
conn.close()
print("Connection closed.")
