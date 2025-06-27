# ESP32 Hacker-Style HTTP Server

A lightweight HTTP server running on an ESP32 using MicroPython, serving a hacker-themed web interface with glitch effects and glowing styles.

---

## Features

- Connects ESP32 to Wi-Fi automatically
- Serves HTML, CSS, images, and other files over HTTP
- Parses HTTP GET requests and serves appropriate files
- Supports text and binary file serving with correct headers
- Hacker-themed UI with green terminal style, glitch animations, and glowing effects
- Simple and extendable architecture

---

## Installation & Setup

1. **Flash MicroPython Firmware on ESP32**

   Download and flash the latest MicroPython firmware for ESP32 from the [official MicroPython site](https://micropython.org/download/esp32/).

2. **Connect ESP32 to Your Computer**

   Use a USB cable and a serial tool (e.g., `screen`, PuTTY) or IDE (e.g., Thonny, uPyCraft).

3. **Upload Project Files**

   Use tools like `ampy`, `rshell`, or IDE upload feature to transfer files to the ESP32 filesystem:

   - `main.py` (your main script)
   - All HTML, CSS, JS, image files needed for the website

4. **Configure Wi-Fi Credentials**

   Edit `main.py` to set your Wi-Fi SSID and password:
   ```python
   SSID = "YOUR_SSID"
   PASSWORD = "YOUR_PASSWORD"

--------------------------------------------------------------------------------------------------------
## Project Structure


/project-root
│
├── main.py               # Main MicroPython script running Wi-Fi & HTTP server
├── index.html            # Default homepage served
├── styles.css            # Hacker style CSS for glowing text, glitch effects
├── hacking.html          # Additional HTML pages
├── painting.html
├── sporten.html
├── js/
│   └── script.js         # Optional JavaScript files
├── images/
│   ├── logo.png
│   └── favicon.ico
└── assets/
    └── [additional assets or files]

--------------------------------------------------------------------------------------------------------

Acknowledgments
Inspired by hacker culture aesthetics and MicroPython's ease of use for embedded web servers.

Feel free to contribute or report issues!

