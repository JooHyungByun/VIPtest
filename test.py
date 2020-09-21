import cv2
# IMREAD_GRAYSCALE
img = cv2.imread('lenna.png', 0)
cv2.imshow('lenna', img)
k = cv2.waitKey(0)
if k == 27: #esc key
    cv2.destroyAllWindows()
elif k == ord('s'): #'s' key
    cv2.imwrite('lenna2.png', 1)
    cv2.destroyAllWindows()


