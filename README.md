# pwm-rc-raspberry-pi-arduino
arduino and raspberry pi controlled rc car/ truck PWM
most controllers will work just edit button values
make sure all parameters are correct specifically to you if you get error(s)
min to max throttle is 0-180
min to max steering is rc vehicle dependent
i used a ps3 controller via bluetooth for button control


i used xpadneo driver for xbox one s controller on rapsbian axis control, but most other controllers will work. just be sure to assign the correct values in the code. for calibrating castle creations esc's, you must turn the esc on while already giving full throttle, after beeps do full reverse, after beeps do neutral. refer to the evdev axis test for determining what axis numbers you have. if you want to also use buttons for your code, replace ABS with KEY. i take no credit for the evdev axis test but i included it for your convenience. when you install nanpy firmware make sure you enable use servo.
