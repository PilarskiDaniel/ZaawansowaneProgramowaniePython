import cv2

image = cv2.imread("bomba.jpg")

(h, w) = image.shape[:2]

lower_half = image[h//2:h, 0:w]

cv2.imshow("Dolna połowa obrazu", lower_half)
cv2.waitKey(0)
cv2.destroyAllWindows()