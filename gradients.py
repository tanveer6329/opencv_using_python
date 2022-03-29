import cv2 as cv 
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('cats', img)

gray =cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('graycale', gray)

# laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('laplacian', lap)


# sobel gradient magnitude regresentation
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combined Sobel with OR', combined_sobel)


cv.waitKey(0)
