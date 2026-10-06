import numpy as np
import cv2 as cv
                                                          
image = cv.imread('img56lab.jpg')
image = cv.resize(image, (800, 450))
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

lower1 = np.array([0,   120, 70]);  upper1 = np.array([10,  255, 255])
lower2 = np.array([170, 120, 70]);  upper2 = np.array([180, 255, 255])
binary = cv.inRange(hsv, lower1, upper1) + cv.inRange(hsv, lower2, upper2)

kernel = np.ones((5, 5), np.uint8)
binary = cv.morphologyEx(binary, cv.MORPH_CLOSE, kernel, iterations=2)
binary = cv.morphologyEx(binary, cv.MORPH_OPEN,  kernel, iterations=1)

sure_bg = cv.dilate(binary, kernel, iterations=3)

dist = cv.distanceTransform(binary, cv.DIST_L2, 5)
_, sure_fg = cv.threshold(dist, 0.2* dist.max(), 255, 0)
sure_fg = np.uint8(sure_fg)

unknown = cv.subtract(sure_bg, sure_fg)

_, markers = cv.connectedComponents(sure_fg)
markers = markers + 1
markers[unknown == 255] = 0

markers = cv.watershed(image, markers)

mask = np.zeros(gray.shape, dtype=np.uint8)
mask[markers > 1] = 255

mask = cv.bitwise_and(mask, binary)

cnts, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
clean = np.zeros_like(mask)
for c in cnts:
    if cv.contourArea(c) > 500:
        cv.drawContours(clean, [c], -1, 255, -1)

result = cv.bitwise_and(image, image, mask=clean)

cv.imshow('Binary mask', binary)
cv.imshow('Watershed markers', np.uint8(markers * 10))
cv.imshow('Result', result)
cv.waitKey(0)
cv.destroyAllWindows()