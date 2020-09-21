import cv2
# GRAY
img = cv2.imread('lenna.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('lenna', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
