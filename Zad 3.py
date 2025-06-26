import cv2
import numpy as np

image = cv2.imread("testo.jpg")
cv2.imshow("Oryginalny obraz", image)

(h, w) = image.shape[:2]

tx = w // 2 + 50
ty = h // 2 + 50

M = np.float32([
    [1, 0, tx],
    [0, 1, ty]
])

shifted = cv2.warpAffine(image, M, (w, h))

cv2.imshow("Przesunięcie > połowy (obraz przesunięty)", shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()