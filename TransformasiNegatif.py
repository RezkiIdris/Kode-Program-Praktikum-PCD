import cv2

img = cv2.imread("stick.jpeg", 0)

img_1 = 255 - img

cv2.imshow("Original Image", img)
cv2.imshow("Image Negatif", img_1)

cv2.waitKey(0)
cv2.destroyAllWindows()