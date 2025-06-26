import cv2
import numpy as np

image = cv2.imread("kp.jpg")

(B, G, R) = cv2.split(image)

# Modyfikacje kanałów:
R = cv2.add(R, 30)
G = cv2.subtract(G, 20)
B = cv2.add(B, 10)

filtered = cv2.merge([B, G, R])

cv2.imshow("Original", image)
cv2.imshow("Instagram Filter", filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()