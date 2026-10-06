import cv2 as cv
import numpy as np

image = cv.imread('img56lab.jpg')
image = cv.resize(image, (800, 450))
image_hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

lower_red1 = np.array([0, 100, 100])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([160, 100, 100])
upper_red2 = np.array([180, 255, 255])

mask1 = cv.inRange(image_hsv, lower_red1, upper_red1)
mask2 = cv.inRange(image_hsv, lower_red2, upper_red2)
mask = mask1 + mask2

result = cv.bitwise_and(image, image, mask=mask)

cv.imshow('Original', image)
cv.imshow('Result', result)

cv.waitKey(0)
cv.destroyAllWindows()