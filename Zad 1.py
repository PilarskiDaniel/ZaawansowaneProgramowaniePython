import cv2
import numpy as np

image = cv2.imread("testo.jpg")
cv2.imshow("Oryginalny obraz", image)

M = np.float32([
    [1, 0, 30],
    [0, 1, 40]
])

shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

cv2.imshow("Przesunięty obraz (30px w prawo, 40px w dół)", shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()