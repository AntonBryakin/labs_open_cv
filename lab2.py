import numpy as np
import cv2

image = cv2.imread('lenna.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

hist = cv2.calcHist([image], [0], None, [256], [0, 256])

cdf = hist.cumsum()

total = cdf[-1]

lut = (cdf / total) * 255
lut = lut.astype(np.uint8).flatten()

result_image = cv2.LUT(image, lut)

cv2.imshow('Original', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Equalized', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()