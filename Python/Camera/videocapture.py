import cv2
import sys
import time

from time import sleep

#print "Before cv2.VideoCapture(0)"
#print cap.grab()
cap = cv2.VideoCapture(0)

ret, frame = cap.read()
if frame is None:
    print("BYE")

while True:
    ret, frame = cap.read()
    if frame is None:
        print("BYE")
        break

    cv2.imshow('frame', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

fourcc = cv2.VideoWriter_fourcc(*'HFYU')
out = cv2.VideoWriter('video.avi',0, 12.5, (640,480))

t0=time.time()
for i in range(100):
    ret, frame = cap.read()
    out.write(frame)
    #cv2.imshow('frame', frame)
    cv2.waitKey(1)
t1=time.time()
print("fps : "+str(100/(t1-t0))+" fps")

out.release()
cap.release()
cv2.destroyAllWindows()
