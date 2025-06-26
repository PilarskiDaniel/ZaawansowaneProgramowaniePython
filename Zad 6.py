import cv2
import imutils

image = cv2.imread("delmito.jpg")
cv2.imshow("Original", image)

resized = imutils.resize(image, height=400)

cv2.imshow("Resized to height 400", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()