import cv2
import imutils

image = cv2.imread("jumper.jpg")
cv2.imshow("Oryginalny obraz", image)

rotated = imutils.rotate_bound(image, -33)

cv2.imshow("Obrócony o -33 stopnie bez przycinania", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()