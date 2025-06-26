import cv2
import numpy as np

image = cv2.imread("win.jpg")

B, G, R = cv2.split(image)

reordered = cv2.merge([R, B, G])

cv2.imshow("Reordered Channels (R, B, G)", reordered)

G_zero = np.zeros_like(G)
modified = cv2.merge([B, G_zero, R])

cv2.imshow("Green Channel Zeroed", modified)

cv2.waitKey(0)
cv2.destroyAllWindows()