import cv2 as cv

# reading images
# img = cv.imread('Photos/cat.jpg')
# cv.imshow('Cat image', img)
# cv.waitKey(0)


# reading videos
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()


