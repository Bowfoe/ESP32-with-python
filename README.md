# ESP32 Hacker-Style HTTP Server

A lightweight HTTP server running on an ESP32 using MicroPython, serving a hacker-themed web interface with glitch effects and glowing styles.

---

## Features

- Connects ESP32 to Wi-Fi automatically on boot (`boot.py`)
- Serves HTML, CSS, images, and other files over HTTP
- Parses HTTP GET requests and serves appropriate files (`analyze_headers.py`)
- Handles sending HTTP responses with correct headers for text and binary files (`response.py`)
- Hacker-themed UI with green terminal style, glitch animations, and glowing effects
- Simple, modular, and extendable architecture

---

## Installation & Setup

### 1. Flash MicroPython Firmware on ESP32

Download and flash the latest MicroPython firmware for ESP32 from the [official MicroPython website](https://micropython.org/download/esp32/).

### 2. Connect ESP32 to Your Computer

Use a USB cable and a serial tool (e.g., `screen`, PuTTY) or an IDE (e.g., Thonny, uPyCraft).

### 3. Upload Project Files

Use tools like `ampy`, `rshell`, `mpremote`, or your IDE's upload feature to transfer files to the ESP32 filesystem:

- `boot.py` — sets up Wi-Fi connection on boot  
- `main.py` — main script running the web server and socket listener  
- `analyze_headers.py` — parses HTTP requests, extracts requested paths and file types  
- `response.py` — prepares and sends HTTP responses  
- Website assets (HTML, CSS, JS, images), e.g., `index.html`, `styles.css`, `js/script.js`, `images/logo.png`

### 4. Configure Wi-Fi Credentials

Edit `boot.py` or `main.py` to set your Wi-Fi SSID and password:

```python
SSID = "YOUR_SSID"
PASSWORD = "YOUR_PASSWORD"

5. Restart ESP32
After uploading all files and configuring Wi-Fi, restart your ESP32 device. The server will start and display the assigned IP address in the console.

/project-root
├── boot.py               # Wi-Fi connection setup on device boot
├── main.py               # Main server script: socket setup, request handling loop
├── analyze_headers.py    # Parses HTTP requests, extracts requested path and file type
├── response.py           # Prepares and sends HTTP responses to clients
├── index.html            # Default homepage served
├── styles.css            # Hacker style CSS for glowing text, glitch effects
├── hacking.html          # Additional HTML pages
├── painting.html
├── sporten.html
├── js/                   # Optional JavaScript files
│   └── script.js
├── images/               # Image assets
│   ├── logo.png
│   └── favicon.ico
└── assets/               # Additional assets or files
