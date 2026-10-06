import cv2
import numpy as np
                                                              
img = cv2.imread('img3lab.jpg', cv2.IMREAD_COLOR)
                                                              
denoised = cv2.medianBlur(img, 5)

result = cv2.bitwise_not(denoised)

cv2.imshow('Original', img)
cv2.imshow('Denoised', denoised)
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()