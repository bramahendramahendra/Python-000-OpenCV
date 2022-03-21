import cv2 as cv

# Read Gambar 
img = cv.imread('gambar/natures.jpg')
cv.imshow('Alam', img)
cv.waitKey(0)

# Read Vidio 
# vidio = cv.VideoCapture('video/v_nature.mp4')
# while True:
#     isTrue, frame = vidio.read()
#     cv.imshow('Vidio Alam', frame)
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break;
# vidio.release()
# cv.destroyAllWindows()



