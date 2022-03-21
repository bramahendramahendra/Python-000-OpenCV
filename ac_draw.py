import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype = 'uint8')
cv.imshow('Blank', blank)
# img = img = cv.imread('gambar/natures.jpg')
# cv.imshow('Alam', img)

# 1. point the image a certain colour
## blank[:] = 0,0,255 
# blank[200:300, 300:400] = 0,0,255
# cv.imshow('Green', blank)

# 2. Draw a rectangle
## cv.rectangle(blank, (0,0), (250,250), (0,250,0), thickness=2)
# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=1)
# cv.imshow('Rectangle', blank)

# 3. draw a circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=1 )
# cv.imshow('Circle', blank)

# 4. Draw a line 
# cv.line(blank, (100,250), (300,400), (255,255,255), thickness=3)
# cv.imshow('Line', blank)

# 5. Write Text 
cv.putText(blank, "Brama Hendra Mahendra", (12,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)