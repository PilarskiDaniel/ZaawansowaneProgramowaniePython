import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")

blue = (255, 0, 0)
red = (0, 0, 255)

center_blue = (40, 40)
cv2.circle(canvas, center_blue, 40, blue, -1)

center_red = (canvas.shape[1] // 2, canvas.shape[0] // 2)
cv2.circle(canvas, center_red, 60, red, -1)

cv2.imshow("Okręgi", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()