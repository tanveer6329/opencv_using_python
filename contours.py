import cv2 as cv 
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('blank image', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray cats', gray)

# canny = cv.Canny(img, 125, 175)
# cv.imshow('canny cats', canny)


ret, thresh = cv.threshold(gray, 125, 255, type=cv.THRESH_BINARY)
cv.imshow("binary image", thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contours found!')

cv.drawContours(blank, contours, -1, (255, 255, 255), 1)
cv.imshow('contour in blank image', blank)

cv.waitKey(0)
