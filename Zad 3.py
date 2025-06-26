import cv2

image = cv2.imread("bomba.jpg")

(h, w) = image.shape[:2]

right_half = image[0:h, w//2:w]

cv2.imshow("Prawa połowa obrazu", right_half)
cv2.waitKey(0)
cv2.destroyAllWindows()