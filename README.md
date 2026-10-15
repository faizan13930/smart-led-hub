# 🌈 Smart LED Hub Controller

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)

Ek simple aur efficient **Smart LED Hub** jo Addressable LEDs (WS2812B, NeoPixel wagera) ko Wi-Fi aur MQTT ke zariye control aur automate karta hai.

---

## 📌 Features
- ⚡ **Multi-Effect Control:** Solid colors, gradients aur dynamic effects.
- 🌐 **Smart Home Integration:** MQTT aur Home Assistant ke sath compatibility.
- ⚙️ **Easy Configuration:** `config.json` ke zariye bina code edit kiye settings change karein.

---

## 🛠 Wiring Diagram

| Controller Pin | LED Strip Pin | Power Supply |
| :--- | :--- | :--- |
| **GPIO 18 / D2** | Data In (DIN) | - |
| **GND** | GND | Common GND (-) |
| **VIN / 5V** | +5V | 5V Power Supply (+) |

> ⚠️ **Note:** Controller aur LED strip ka Ground (GND) hamesha aapas me connected (common) hona zaroori hai.

---

## 🚀 Quick Installation

1. **Repository clone karein:**
   ```bash
   git clone https://github.com/faizan13930/smart-led-hub.git
   cd smart-led-hub
   ```

2. **Dependencies install karein:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Controller run karein:**
   ```bash
   python controller.py
   ```

---

## 📜 License
This project is licensed under the MIT License.
