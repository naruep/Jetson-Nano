import cv2
from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)

cap = cv2.VideoCapture(0)


width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print('width:', width, 'height', height)

face_cascade = cv2.CascadeClassifier(
    '/home/jay/Desktop/pythonProject/cascade/face.xml')
# eye_cascade = cv2.CascadeClassifier(
#     '/home/jay/Desktop/pythonProject/cascade/eye.xml')

pan = 90
tilt = 10

kit.servo[0].angle = pan
kit.servo[1].angle = tilt

while cap.isOpened():
    ok, image = cap.read()
    image = cv2.flip(image, 2)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        Xcent = x+w/2
        Ycent = y+h/2
        errorPan = Xcent-width/2
        errorTilt = Ycent-height/2
        if errorPan > 0:
            pan = pan-1
        if errorPan < 0:
            pan = pan+1
        if errorTilt > 0:
            tilt = tilt-1
        if errorTilt < 0:
            tilt = tilt+1
        if pan > 180:
            pan = 180
            print("Pan Out of Range")
        if pan < 0:
            pan = 0
            print("Pan Out of Range")
        if tilt > 180:
            tilt = 180
            print("Tilt Out of Range")
        if tilt < 0:
            tilt = 0
            print("Tilt Out of Range")
        kit.servo[0].angle = pan
        # kit.servo[1].angle = tilt

        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0))
        # roi_gray = gray[y:y+h, x:x+w]
        # Roi_color = image[y:y+h, x:x+w]
        # eyes = eye_cascade.detectMultiScale(roi_gray)
        # for (xEye, yEye, wEye, hEye) in eyes:
        #     cv2.circle(Roi_color, (int(xEye+wEye/2), int(yEye+hEye/2)),
        #                6, (0, 0, 255), -1)

    cv2.imshow('WebCam', image)

    k = cv2.waitKey(1) & 0xFF
    if (k == 27):
        break

cv2.moveWindow('WebCam', 0, 0)
cap.release()
cv2.destroyAllWindows()
