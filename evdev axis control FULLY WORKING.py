import serial
from evdev import InputDevice, categorize, ecodes
from nanpy import Servo

#asign pin out for each servo device
throttle = Servo(11)
steering = Servo(10)
ser1 = serial.Serial('/dev/ttyUSB0', 115200, timeout=0.001)

#linux only, select event#
gamepad = InputDevice('/dev/input/event1')
print(gamepad)
for event in gamepad.read_loop():
    
    if event.type == ecodes.EV_ABS:
        #select x axis left stick#
        if event.code == 0:
            steering_in = event.value
            #find center(165) start 180, divided by controller maximum#
            steering_out = 165*steering_in/65535
            #if axis goes full left and right, divide by 2 and go from there
            #if no longer centered, add or subtract a number until it is again
            steeringout = steering_out/2+45
            steering.write(steeringout)
        #select left trigger#
        if event.code == 2:
            brake_in = event.value
            #if full press is neutral, subtract 90
            #divide by controller maximum and multiply by 90
            #assuming full reverse value is 0
            brake_out = 90-(90*brake_in/1023)
            throttle.write(brake_out)
            
        if event.code == 5:
            throttle_in = event.value
            #if full press is neutral, add 90 to get 180
            #divide by controller maximum and multiply by 90
            #assuming full throttle is 180
            throttle_out = 90+(90*throttle_in/1023)
            throttle.write(throttle_out)
