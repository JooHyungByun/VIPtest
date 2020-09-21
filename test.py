import cv2
img = cv2.imread('lenna.png', 1) # IMREAD_COLOR
cv2.imshow('lenna', img)
cv2.waitKey(0)