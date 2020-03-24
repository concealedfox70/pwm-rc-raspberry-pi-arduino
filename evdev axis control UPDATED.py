import serial
from nanpy import Servo
from evdev import InputDevice, categorize, ecodes
## replace event number with your controller
gamepad = InputDevice('/dev/input/event8')
print(gamepad)

throttle = Servo(11)
steering = Servo(10)
##if you do not use a camera gimbal comment next line out
gimbal = Servo(9)

##make sure this matches the arduino
ser1 = serial.Serial('/dev/ttyUSB0', 115200, timeout=0.001)

for event in gamepad.read_loop():

    if event.type == ecodes.EV_ABS:
##select x axis left stick
        if event.code == 0:
##replace 2047 with your controller's max value for all 3
            steering = event.value/2047*180
##trim steering value as needed here
            steering = steering-0
            steering.write(steering)
##comment out controls for either right stick or triggers

##right stick throttle
##select y axis right stick
        elif event.code == 1:
            throttle = event.value/2047*180
            throttle.write(throttle)

##left right triggers throttle
##only use 1 trigger at a time
##select left trigger            
        elif event.code == 2:
            brake = event.value
            brake = 90-(90*brake/1023)
            throttle.write(brake)
##select right trigger            
        elif event.code == 5:
            throttle = event.value
            throttle = 90+(90*throttle/1023)
            throttle.write(throttle)
##comment out this section if camera gimbal isnt used
        elif event.code == 3:
            gimbal = event.value/2047*180
            gimbal.write(gimbal)
