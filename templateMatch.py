import numpy as np
import cv2

img = cv2.imread('TwTim/soccer_practice.jpg',0)
template = cv2.imread('TwTim/ball.png',0)
#template = cv2.imread('TwTim/shoe.png',0)
h,w = template.shape


methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()
    img3 = cv2.imread('TwTim/soccer_practice.jpg')
    result = cv2.matchTemplate(img2,template,method)       #performs convolution to match our template with the base image returns array (W - w+1, H- h +1) using function method
    minVal,maxVal,minLoc,maxLoc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = minLoc
    else:
        location = maxLoc

    bottom_right = (location[0] + w, location[1] + h)    #to calculate bottom left corner of rectangle to draw when matched 
    cv2.rectangle(img3, location, bottom_right, 255, 5)
    cv2.imshow('Match', img3)

    cv2.waitKey(0)

    cv2.destroyAllWindows()
# we observe different methods found the ball except the third one ie TM CCORR.