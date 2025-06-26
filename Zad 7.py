import cv2
import imutils
import numpy as np

image = cv2.imread("jumper.jpg")
cv2.imshow("Oryginalny obraz", image)

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

M = cv2.getRotationMatrix2D((cX, cY), 60, 1.0)
rotated_warp = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Obrócony 60 stopni - warpAffine", rotated_warp)

rotated_imutils = imutils.rotate(image, 60)
cv2.imshow("Obrócony 60 stopni - imutils.rotate", rotated_imutils)

cv2.waitKey(0)
cv2.destroyAllWindows()