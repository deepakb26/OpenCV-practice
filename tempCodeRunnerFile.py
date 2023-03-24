import numpy as np
import cv2

img = cv2.imread("soccer_practice.jpg",0)
template = cv2.imread("ball.jpg",0)
h,w = template.shape()
