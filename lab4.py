import cv2
import numpy as np
                                                              
img = cv2.imread('img4lab.png', 0)
                                                              
_, binimg = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY) 
binimg = cv2.bitwise_not(binimg) 
kernel = np.ones((4, 1), np.uint8)                      
result = cv2.morphologyEx(binimg, cv2.MORPH_CLOSE, kernel, iterations=2)                                 
result = cv2.bitwise_not(result) 
                                    
cv2.imshow('Original', img)
cv2.imshow('Image1', binimg)
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()