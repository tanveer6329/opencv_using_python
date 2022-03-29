import cv2 as cv 

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

# averaging
average = cv.blur(img, (7, 7))
cv.imshow('average blur', average)

# gaussian blur
gauss = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow('gaussian blur', gauss)

# median blur
median = cv.medianBlur(img, 3)
cv.imshow('median blur', median)

# bilateral
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('bilateral filter', bilateral)


cv.waitKey(0)
