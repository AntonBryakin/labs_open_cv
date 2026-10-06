import cv2 as cv
import numpy as np

img = cv.imread('img7lab.jpg')
template = cv.imread('img7tmpl.jpg')

img = cv.resize(img, (img.shape[1]//2, img.shape[0]//2), interpolation=cv.INTER_AREA)
template = cv.resize(template, (template.shape[1]//2, template.shape[0]//2), interpolation=cv.INTER_AREA)

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray_templ = cv.cvtColor(template, cv.COLOR_BGR2GRAY)

w, h = template.shape[1], template.shape[0]

res = cv.matchTemplate(gray_img, gray_templ, cv.TM_CCOEFF_NORMED)

threshold = 0.8
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
    cv.rectangle(img, pt, (pt[0] + w, pt[1] + h), (255, 0, 0), 2)
                        
cv.imshow('Result', img)
cv.waitKey(0)
cv.destroyAllWindows()