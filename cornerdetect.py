import numpy as np
import cv2

img = cv2.imread('chessboard.png')
img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)  #resize
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    #grayscale it

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10) #100 corners, minimum quality of corners minimum distance b/w two corners
#returns float aarray
corners = np.int0(corners) #convert to integer arrays

# finds corners using algorithm on Grayscale

for corner in corners:
	x, y = corner.ravel()       #flattens array ie removes nested array  ie makes 2D to 1D array
	cv2.circle(img, (x, y), 5, (255, 0, 0), -1) #draws circle with centre xy radius 5 and fills it using blue
	#draws the circles on original coloured image

for i in range(len(corners)):
	for j in range(i + 1, len(corners)):
		corner1 = tuple(corners[i][0])
		corner2 = tuple(corners[j][0])
		color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
		cv2.line(img, corner1, corner2, color, 1)

cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()