import cv2
import imutils

image = cv2.imread("jumper.jpg")
cv2.imshow("Oryginalny obraz", image)

rotated = imutils.rotate(image, 180)

cv2.imshow("Obrócony o 180 stopni", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()