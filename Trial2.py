# Hack. :)
import site; site.addsitedir("/usr/local/lib/python2.7/site-packages")

import cv2
import cv2.cv as cv
import numpy as np

img = cv2.imread('test-images/still1.jpg', 0)
# img = cv2.medianBlur(img,5)

blurry = cv2.GaussianBlur(img, (15, 15), 20)
cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(blurry,
                           cv.CV_HOUGH_GRADIENT,
                           1,
                           len(img[0])/5,
                           param1=50, param2=30, minRadius=10, maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
