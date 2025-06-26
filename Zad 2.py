import cv2
import numpy as np

image = cv2.imread("kp.jpg")

M = np.ones(image.shape, dtype="uint8") * 150

burned_numpy = image + M

burned_opencv = cv2.add(image, M)

cv2.imshow("Original", image)
cv2.imshow("Overexposed (NumPy)", burned_numpy)
cv2.imshow("Overexposed (OpenCV)", burned_opencv)
cv2.waitKey(0)
cv2.destroyAllWindows()