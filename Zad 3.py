import cv2
import numpy as np

image = cv2.imread("kp.jpg")

M = np.ones(image.shape, dtype="uint8") * 80

dark_numpy = image - M

dark_opencv = cv2.subtract(image, M)

cv2.imshow("Original", image)
cv2.imshow("Darker (NumPy)", dark_numpy)
cv2.imshow("Darker (OpenCV)", dark_opencv)
cv2.waitKey(0)
cv2.destroyAllWindows()