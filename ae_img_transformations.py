import cv2 as cv
import numpy as np

img = cv.imread('gambar/natures.jpg')
cv.imshow('Gambar', img)

# Translation 
def translate(img, x, y):
    translateMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, translateMat, dimensions)

# -x = left 
# -y = up
# X = right
# y = bottom
img_translated = translate(img, -100, 100)
cv.imshow('Image Translated', img_translated)


# Rotation 
def rotate(img, angle, rotPoint = None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width //2, height //2)
    rotatioMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotatioMat, dimensions)

img_rotated = rotate(img, -45)
cv.imshow("Image rotation", img_rotated)

img_rotated_rotated = rotate(img_rotated, -105)
cv.imshow("Image rotation rotation", img_rotated_rotated)

# FLipping 
img_flip = cv.flip(img, -1)
cv.imshow("Image Flip", img_flip)

cv.waitKey(0)
