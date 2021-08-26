import cv2
# from adafruit_servokit import ServoKit
import time

# myKit = ServoKit(channels=16)
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

face_cascade = cv2.CascadeClassifier(
    '/home/jay/Desktop/pythonProject/cascade/face.xml')
eye_cascade = cv2.CascadeClassifier(
    '/home/jay/Desktop/pythonProject/cascade/eye.xml')

# myKit.servo[0].angle = 90
# myKit.servo[1].angle = 10

while cap.isOpened():
    ok, image = cap.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0))
        roi_gray = gray[y:y+h, x:x+w]
        Roi_color = image[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (xEye, yEye, wEye, hEye) in eyes:
            cv2.circle(Roi_color, (int(xEye+wEye/2), int(yEye+hEye/2)),
                       4, (0, 0, 255), -1)

    cv2.imshow('WebCam', image)

    k = cv2.waitKey(1) & 0xFF
    if (k == 27):
        break

cv2.moveWindow('WebCam', 0, 0)
cap.release()
cv2.destroyAllWindows()
