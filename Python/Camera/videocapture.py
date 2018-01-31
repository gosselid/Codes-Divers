import cv2
import sys

from time import sleep

#print "Before cv2.VideoCapture(0)"
#print cap.grab()
cap = cv2.VideoCapture(0)

ret, frame = cap.read()
if frame is None:
    print("BYE")

fourcc = cv2.VideoWriter_fourcc(*'HFYU')
out = cv2.VideoWriter('video2.avi',0, 20.0, (640,480))

for i in range(20):
    ret, frame = cap.read()
    out.write(frame)
    cv2.imshow('frame', frame)
    cv2.waitKey(1)

retval	=	cv2.VideoWriter.get()

out.release()
cap.release()
cv2.destroyAllWindows()
