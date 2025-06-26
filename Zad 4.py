import cv2
import numpy as np

image = cv2.imread("win.jpg")

B, G, R = cv2.split(image)

R_boosted = cv2.add(R, 50)

boosted_image = cv2.merge([B, G, R_boosted])

cv2.imshow("Original Image", image)
cv2.imshow("Red Channel Boosted", boosted_image)

cv2.waitKey(0)
cv2.destroyAllWindows()