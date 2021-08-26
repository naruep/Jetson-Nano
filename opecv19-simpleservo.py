import cv2
from adafruit_servokit import ServoKit
import time

myKit = ServoKit(channels=16)
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

myKit.servo[0].angle = 90
myKit.servo[1].angle = 10

while cap.isOpened():
    ok, image = cap.read()

    cv2.imshow('WebCam', image)

    k = cv2.waitKey(1) & 0xFF
    if (k == 27):
        break

cv2.moveWindow('WebCam', 0, 0)
cap.release()
cv2.destroyAllWindows()