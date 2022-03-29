import cv2 as cv

img = cv.imread('Photos\cat.jpg')

cv.imshow('cat', img)

# converting an image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# blur
# blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# edge cascade
# canny = cv.Canny(img, 125, 175)
# cv.imshow('Canny edges', canny)

# dilating the image
# dilated = cv.dilate(canny, (3, 3), iterations=1)
# cv.imshow('Dilated', dilated)

# eroding
# eroded = cv.erode(dilated, (3, 3), iterations=1)
# cv.imshow('Eroded', eroded)

# resize
# resized = cv.resize(img, (500, 500))
# cv.imshow('Resized', resized)

# cropping
# cropped = img[0:200, 0:200]
# cv.imshow('Cropped', cropped)

cv.waitKey(0)