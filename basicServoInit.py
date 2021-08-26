from adafruit_servokit import ServoKit
Kit = ServoKit(channels=16)

# Control Camera Pan to 90 degree
kit.servo[0].angle = 90

# Control Camera Tilt to 90 degree
kit.servo[1].angle = 90
