import cv2
import sys

from time import sleep

#print "Before cv2.VideoCapture(0)"
#print cap.grab()
cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
fgbg.setVarThreshold(30)

print(fgbg.getVarThreshold())

for i in range(10):
    ret,frame = cap.read()
    fgmask = fgbg.apply(image=frame)
    cv2.imshow('frame',fgmask)

while True:
    ret, frame = cap.read()
    if frame is None:
        print("BYE")
        break

    fgmask = fgbg.apply(image=frame,learningRate=0)
    cv2.imshow('frame',fgmask)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

fgbg.setVarThreshold(30)
print(fgbg.getVarThreshold())

for i in range(10):
    ret,frame = cap.read()
    fgmask = fgbg.apply(image=frame)
    cv2.imshow('frame',fgmask)

while True:
    ret, frame = cap.read()
    if frame is None:
        print("BYE")
        break

    fgmask = fgbg.apply(image=frame,learningRate=0)
    cv2.imshow('frame',fgmask)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
