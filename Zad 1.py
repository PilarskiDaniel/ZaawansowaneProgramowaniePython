import cv2
import numpy as np

image = cv2.imread("jumper.jpg")
cv2.imshow("Oryginalny obraz", image)

(h, w) = image.shape[:2]
center = (w // 2, h // 2)

M = cv2.getRotationMatrix2D(center, 45, 1.0)

rotated = cv2.warpAffine(image, M, (w, h))

cv2.imshow("Obraz obrócony o 45 stopni", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()