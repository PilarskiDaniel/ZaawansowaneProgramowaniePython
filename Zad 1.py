import cv2
import numpy as np

image = cv2.imread("kp.jpg")

M = np.ones(image.shape, dtype="uint8") * 50

brighter_cv = cv2.add(image, M)

brighter_np = image + M
cv2.imshow("Original", image)
cv2.imshow("Brighter (OpenCV)", brighter_cv)
cv2.imshow("Brighter (NumPy)", brighter_np)
cv2.waitKey(0)
cv2.destroyAllWindows()