# 🛠 Hackpad
### A DIY 4x4 RGB Macropad built with Seeed XIAO RP2040

![Status](https://img.shields.io/badge/status-in%20development-orange)
![Platform](https://img.shields.io/badge/platform-RP2040-blue)
![Firmware](https://img.shields.io/badge/firmware-CircuitPython-green)
![License](https://img.shields.io/badge/license-Open%20Source-lightgrey)

---

## 📌 Overview

Hackpad is a fully custom 4x4 mechanical macropad with RGB lighting.  
It is powered by the **Seeed XIAO RP2040** and acts as a programmable USB HID macro device.

Designed for:
- 🎬 Video editing
- 💻 Coding shortcuts
- 🎛 Sound & light control
- 🎮 Streaming
- ⚡ Productivity workflows

---

## 📸 Project Screenshots

### 🔹 Overall Hackpad (real photo when parts arrive)
![Overall Hackpad](images/hackpad_case.png)


---

### 🔹 Schematic
![Schematic](images/hackpad_schematic.png)

---

### 🔹 PCB Layout
![PCB](images/hackpad_pcb.png)

---

### 🔹 PCB 3D View
![PCB](images/hackpad_pcb_3d.png)

---

### 🔹 Case Design & Assembly
![Case](images/hackpad_case.png)

The enclosure:
- Holds the PCB securely  
- Supports the XIAO module  
- Allows USB-C access  
- Uses M3 screws for assembly  

---

## ⚙️ Hardware Specifications

- 4x4 key matrix
- 16x SK6812 MINI-EA RGB LEDs
- 16x 1N4148 diodes (anti-ghosting)
- USB-C powered
- Fully programmable firmware
- RGB control

---

## 🧾 Bill of Materials (BOM)

| Qty | Component | Description |
|-----|----------|------------|
| 1 | Seeed XIAO RP2040 | Microcontroller |
| 16 | MX-style switches | Mechanical key switches |
| 16 | SK6812 MINI-E | Addressable RGB LEDs |
| 16 | 1N4148 | Switching diodes |
| 1 | Custom PCB | Designed in EasyEDA |
| 1 | 3D Printed Case | Custom enclosure |
| 16 | Keycaps | MX compatible |
| 4 | M3 screws | Case mounting |
| 4 | M3 heatset inserts | Case mounting |
| 1 | USB-C cable | Power & data |

---

## 💻 Firmware

Hackpad runs **CircuitPython** and functions as a USB HID device.

### Features
- Matrix scanning
- RGB lighting control
- Custom macros

### Planned Features
- Multiple macro layers
- Profile saving

---

## 🛠 Tools Used

- EasyEDA (Schematic & PCB)
- Fusion 360 (Case design)
- CircuitPython (Firmware)
- 3D Printing (Enclosure)

---

## 🚀 Project Goals

This project was built to:

- Learn PCB design
- Design a key matrix with diodes
- Implement RGB LED control
- Build a custom USB HID device
- Gain embedded systems experience


