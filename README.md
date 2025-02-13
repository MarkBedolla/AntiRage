# Sound Sensor Arduino Project

## Parts Needed
- **Arduino Uno** (with a USB A to B cable)  
- **KY-038 Sound Sensor Module**  
- **LED**  
- **Jumper Wires** (female-to-male)  
- **Flat Head Screwdriver** (to adjust the potentiometer of the sound sensor)  

## Wiring Instructions

1. Take **three jumper wires** and connect them to the headers of the KY-038 sensor module:
   - **GND (G)** → Ground  
   - **VCC (+)** → Power  
   - **DO (Digital Output)** → Digital Signal  

2. Connect the other side of the jumper wires to the **Arduino Uno**:
   - **VCC (+) → 5V**  
   - **GND → Any GND Pin**  
   - **DO → Pin 2**  

3. Connect the **LED**:
   - **Longer lead (positive)** → **Pin 13**  
   - **Shorter lead (ground)** → **GND**  

### Setting Up the Arduino

1. Connect the **Arduino Uno** to your computer using the USB cable.  
2. Download and install the **Arduino IDE** from [here](https://www.arduino.cc/en/software).  
3. Open the Arduino IDE and **select the correct port** for your Arduino board.  
4. Use code I have provided. 

### Adjusting the Sound Sensor Sensitivity
Use a **flat head screwdriver** to **adjust the potentiometer** on the KY-038 sound sensor module. This will modify its sensitivity to sound.  

## Troubleshooting
If you're having trouble setting this up, check out this video tutorial:  
[![Video Guide](https://img.youtube.com/vi/a1Kp1OtSwu8/0.jpg)](https://youtu.be/a1Kp1OtSwu8?si=kXYt0FaZDNoN5C5H)  
---

Now your setup is ready to detect sound levels! 🎛️🔊  
