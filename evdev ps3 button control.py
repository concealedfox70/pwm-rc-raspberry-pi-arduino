import serial
from evdev import InputDevice, categorize, ecodes
from nanpy import Servo

throttle = Servo(11)
steering = Servo(10)
ser1 = serial.Serial('/dev/ttyUSB0', 115200, timeout=0.001)
gamepad = InputDevice('/dev/input/event2')
print(gamepad)

for event in gamepad.read_loop():
    
    if event.type == ecodes.EV_KEY:
        if event.value == 1:            
            if event.code == 312:
                throttle.write(10)
            if event.code == 313:
                throttle.write(150)
            if event.code == 546:
                steering.write(55)
            if event.code == 547:
                steering.write(125)
        elif event.value == 0:
            if event.code == 312:
                throttle.write(90)
            if event.code == 313:
                throttle.write(90)
            if event.code == 546:
                steering.write(86)
            if event.code == 547:
                steering.write(86)
