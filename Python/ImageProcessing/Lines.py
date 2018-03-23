import cv2
import numpy as np
from matplotlib import pyplot as plt




img = cv2.imread('2o10c.jpg',1)
b,g,r= cv2.split(img)
img=r.copy()
img[:]=0

edges = cv2.Canny(r,20,80,apertureSize = 3)

lines = cv2.HoughLinesP(edges,1,np.pi/180,20)
for x1,y1,x2,y2 in lines[:,0]:
        cv2.line(r,(x1,y1),(x2,y2),(0,0,255),2)
        cv2.line(img,(x1,y1),(x2,y2),(255,255,255),2)


edges = cv2.Canny(img,20,80,apertureSize = 3)

lines = cv2.HoughLines(img,1,np.pi/180,50)

for rho,theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    cv2.line(img,(x1,y1),(x2,y2),(150,150,150),2)

cv2.imshow('detected circles',r)
cv2.waitKey(0)
cv2.imshow('houghlines3.jpg',img)
cv2.waitKey(0)
print(cv2.minMaxLoc(img))
