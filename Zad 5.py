import cv2
import imutils

image = cv2.imread("delmito.jpg")
cv2.imshow("Original", image)

resized = imutils.resize(image, width=500)

# Wyświetlenie wyniku
cv2.imshow("Resized to width 500", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()