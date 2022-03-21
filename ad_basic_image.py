import cv2 as cv

img = img = cv.imread('gambar/natures.jpg')
cv.imshow('Gambar', img)

# Converting to grayscyle 
gambar_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gambar Gray', gambar_gray)

# Blur 
gambar_blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Gambar Blur', gambar_blur)

# Edge Cascade 
gambar_canny = cv.Canny(gambar_blur, 125, 175)
cv.imshow('Gambar Canny', gambar_canny)

# Dilating the Image
gambar_dilated = cv.dilate(gambar_canny, (7,7), iterations=3)
cv.imshow('Gambar dilating', gambar_dilated)

# Eroding 
gambar_eroding = cv.erode(gambar_dilated, (7,7), iterations=3)
cv.imshow('Gambar Eroded', gambar_eroding)

# Resize 
gambar_resize = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Gambar resize', gambar_resize)

# Cropping 
gambar_cropping = img[50:200, 200:400]
cv.imshow('Gambar Cropping', gambar_cropping)



cv.waitKey(0)