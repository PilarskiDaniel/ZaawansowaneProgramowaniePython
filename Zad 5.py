import cv2
import numpy as np

tx = int(input("Podaj przesunięcie w poziomie (tx): "))
ty = int(input("Podaj przesunięcie w pionie (ty): "))

image = cv2.imread("testo.jpg")
cv2.imshow("Oryginalny obraz", image)

M = np.float32([[1, 0, tx], [0, 1, ty]])

shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

cv2.imshow(f"Przesunięcie o ({tx}, {ty})", shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()