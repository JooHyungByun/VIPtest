import cv2
# GRAY
img = cv2.imread('lenna.png', 0) # Conflict TEST
cv2.imshow('lenna', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
