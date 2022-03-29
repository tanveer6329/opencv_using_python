import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')


img = cv.imshow('blank', blank)

# blank[:] = 0,0, 255
# cv.imshow('blank2', blank)

cv.rectangle(blank, (0,0), (255, 255), (255, 0, 0), thickness=cv.FILLED)
cv.imshow('rectangle', blank)

cv.circle(blank, (255, 255), 100, (0, 0, 255), thickness=cv.FILLED)
cv.imshow('circle', blank)

cv.line(blank, (0, 0), (255, 255), (255, 255, 255), thickness=1)
cv.imshow('line', blank)

cv.putText(blank, "Hello", (200, 200), fontFace=cv.FONT_HERSHEY_TRIPLEX, fontScale=1.0, color=(0, 255, 0), thickness=2)
cv.imshow('text', blank)

cv.waitKey(0)