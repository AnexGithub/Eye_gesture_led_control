# 👁️ Eye Gesture Controlled LED using OpenCV and Arduino

This project allows you to control an **AC-powered LED bulb** using **eye gestures** detected via a laptop camera. The gestures are processed using **OpenCV**, and a signal is sent to an **Arduino** to toggle a relay module controlling the AC LED.

---

## Components Required

| Component              | Quantity | Description                                         |
|------------------------|----------|-----------------------------------------------------|
| Arduino Uno            | 1        | Microcontroller board                               |
| Relay Module (5V)      | 1        | For switching the AC LED bulb                       |
| AC LED Bulb            | 1        | Connected via the relay                             |
| Laptop with Camera     | 1        | Used to capture eye gestures                        |
| USB Cable              | 1        | For connecting Arduino to laptop                    |
| Jumper Wires           | -        | For connections                                     |
| 1K Ohm Resistor (optional) | 1    | For LED testing during development                  |

---

## Working Principle

- **Eye Gesture Detection**: Uses OpenCV and `dlib` to detect blinking or eye winks.
- **Communication**: Python sends serial signals (`'1'` or `'0'`) to Arduino via USB.
- **Arduino Control**: The Arduino reads the serial input and toggles the relay, switching the AC LED bulb ON or OFF accordingly.

---

## Circuit Diagram

[Relay Module]
|
|----- IN pin -> Arduino Digital Pin 10
|----- VCC -> 5V (Arduino)
|----- GND -> GND (Arduino)

[AC LED Bulb]
|----- Live wire -> Relay COM
|----- Relay NO -> AC Live
|----- Neutral wire -> Direct to AC Neutral


**WARNING: Handle AC connections with extreme caution. Ensure power is disconnected when wiring.**

---

## Software Setup

### 1. Python Libraries Installation

Make sure you have Python 3 installed. Then install the required packages:

```bash
pip install opencv-python dlib imutils pyserial

