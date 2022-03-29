import cv2 as cv 
import matplotlib.pyplot as plt

img = cv.imread('Photos/park.jpg')
cv.imshow('park', img)

plt.imshow(img)
plt.show()

# bgr image to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('grayscale', gray)

# BGR TO HSV
# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('hsv', hsv)

# BGR TO L*a*b
# lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('lab', lab)

# cv.waitKey(0)
