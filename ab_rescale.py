import cv2 as cv
from cv2 import resize

# function rescale 
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# Read Gambar 
img = cv.imread('gambar/natures.jpg')
cv.imshow('Alam', img)
# get function rescale 
resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)
cv.waitKey(0)


# Read Vidio 
# vidio = cv.VideoCapture('video/v_nature.mp4')
# while True:
#     isTrue, frame = vidio.read()
#     frame_resized = rescaleFrame(frame, scale=2)
#     cv.imshow('Vidio Alam', frame)
#     cv.imshow('Vidio Alam Resize', frame_resized)
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break;
# vidio.release()
# cv.destroyAllWindows()
 