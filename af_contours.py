import cv2 as cv

img = cv.imread('gambar/natures.jpg')
cv.imshow('Gambar', img)

# Gray 
gambar_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gambar Gray', gambar_gray)

# Edge Cascade 
gambar_canny = cv.Canny(img, 125, 175)
cv.imshow('Gambar Canny', gambar_canny)

contours, hierarchies = cv.findContours(gambar_canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour (s) found!') 
