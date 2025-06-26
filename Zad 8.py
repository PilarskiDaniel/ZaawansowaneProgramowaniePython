import cv2
import numpy as np

image = cv2.imread("jumper.jpg")
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

def rotate_image(img, angle):
    M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
    return cv2.warpAffine(img, M, (w, h))

rotated_seq = image.copy()
for _ in range(3):
    rotated_seq = rotate_image(rotated_seq, 30)

rotated_single = rotate_image(image, 90)

cv2.imshow("Oryginalny obraz", image)
cv2.imshow("Sekwencyjny obrót 3x30 stopni", rotated_seq)
cv2.imshow("Pojedynczy obrót 90 stopni", rotated_single)

cv2.waitKey(0)
cv2.destroyAllWindows()