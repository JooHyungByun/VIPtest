import cv2
# IMREAD_GRAYSCALE
img = cv2.imread('lenna.png', 0)
cv2.imshow('lenna', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
