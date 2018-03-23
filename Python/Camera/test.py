import cv2
import sys

from time import sleep

#print "Before cv2.VideoCapture(0)"
#print cap.grab()
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if frame is None:
        print("BYE")
        break

    cv2.imshow('frame', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
