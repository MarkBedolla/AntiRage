import serial
import os
import time
import tkinter as tk
from tkinter import messagebox

# Replace 'COM3' with the port your Arduino is connected to
arduino_port = 'COM3'
baud_rate = 9600

def show_warning_message(message, title, image_path=None):
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    if image_path:
        img = tk.PhotoImage(file=image_path)
        panel = tk.Label(root, image=img)
        panel.pack(side="top", fill="both", expand="yes")
    messagebox.showwarning(title, message)
    root.destroy()

def shutdown_computer():
    print("Shutting down computer in 10 seconds...")
    time.sleep(10)  # Delay to give you time to cancel if needed
    os.system("shutdown /s /t 1")  # Shutdown in 1 second

if __name__ == '__main__':
    try:
        ser = serial.Serial(arduino_port, baud_rate)
        time.sleep(2)  # Give some time for the serial connection to establish

        warning_shown = False

        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').strip()
                print(f"Received: {line}")  # For debugging

                if line == "NOISE_DETECTED":
                    if not warning_shown:
                        print("First NOISE_DETECTED signal received")
                        show_warning_message("Stop raging at a video and go make friends. Stop being a disappointment to your family.", "1st warning")
                        warning_shown = True
                    else:
                        print("Second NOISE_DETECTED signal received")
                        show_warning_message("Another loud noise detected dipshit I warned your stupid ahh to pipe down. Your shit of a PC will shut down in 10 seconds.", "Final Warning to the fat idiot raging!")
                        shutdown_computer()
                        break  # Exit loop after initiating shutdown
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
    except KeyboardInterrupt:
        print("Program interrupted by user.")
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()
