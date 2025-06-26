import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")

(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)

blue = (255, 0, 0)

cv2.line(canvas, (centerX, centerY), (299, 299), blue, 2)

cv2.imshow("Niebieska linia", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
