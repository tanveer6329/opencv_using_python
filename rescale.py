import cv2 as cv


def rescaleFrame(frame, scale=0.75):
	width = int(frame.shape[1] * scale)
	height = int(frame.shape[0] * scale)
	dimensions = (width, height)

	return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)



def changeRes(width, height):



# reading images
img = cv.imread('Photos/cat_large.jpg')
cv.imshow('Cat image', img)

frame_resized = rescaleFrame(img, scale=0.3)
cv.imshow('cat resized image', frame_resized)
cv.waitKey(0)






# reading videos
# capture = cv.VideoCapture('Videos/dog.mp4')

# while True:
#     isTrue, frame = capture.read()

#     frame_resized =  rescaleFrame(frame, scale=0.5)

#     cv.imshow('video', frame)
#     cv.imshow('video_resized', frame_resized)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()