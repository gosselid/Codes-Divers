import cv2
import numpy as np
from matplotlib import pyplot as plt
from math import sqrt


img = cv2.imread('1o10.jpg',1)
b,g,r= cv2.split(img)
img_used=r
cv2.imshow('detected circles',img_used)
cv2.waitKey(0)
[Cmin, Cmax,pos_min, pos_mx] = cv2.minMaxLoc(img_used)
img_used=np.uint8(np.around(np.minimum((img_used-Cmin)*255/(np.mean(r)-Cmin),255)))
cv2.imshow('detected circles',img_used)
cv2.waitKey(0)
img_used = cv2.medianBlur(img_used,5)

circles = cv2.HoughCircles(img_used,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=25,minRadius=25,maxRadius=50)

circles = np.int16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(img_used,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(img_used,(i[0],i[1]),2,(0,0,255),3)


cv2.imshow('detected circles',img_used)
cv2.waitKey(0)

first = True
i0=0
i1=0
for i in circles[0,:]:
	print(i[2])
	if not first:
		print("Length (between radii centers) : ")
		print(sqrt((i[0]-i0)**2+(i[1]-i1)**2))
	i0=i[0]
	i1=i[1]
	first=False
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#exit(0)
