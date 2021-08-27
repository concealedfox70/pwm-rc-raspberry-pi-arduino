from inputs import get_gamepad
from nanpy import Servo

value_x = 90
value_rx = 90
value_ry = 90

throttle = Servo(*match arduino pwm wiring here*)
steering = Servo(*match arduino pwm wiring here*)
gimbal = Servo(*match arduino pwm wiring here if used*)
while True:
        events = get_gamepad()
        for event in events:
                if event.code == 'ABS_X':
                        value_x = round(90+(event.state/32767)*90, 3)
                        steering.write(value_x)
                if event.code == 'ABS_RX':  ##gimbal only
                        value_rx = round(90+(event.state/32767)*90, 3)
                        throttle.write(value_y)
                if event.code == 'ABS_RY':
                        value_ry = round(90+(event.state/32767)*90, 3)
                        throttle.write(value_ry)
