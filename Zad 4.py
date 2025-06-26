import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")

white = (255, 255, 255)
blue = (255, 0, 0)

centerX, centerY = canvas.shape[1] // 2, canvas.shape[0] // 2

square_size = 100
top_left = (centerX - square_size // 2, centerY - square_size // 2)
bottom_right = (centerX + square_size // 2, centerY + square_size // 2)

cv2.rectangle(canvas, top_left, bottom_right, white, 2)

cv2.circle(canvas, (centerX, centerY), 30, blue, -1)

cv2.imshow("Kwadrat i okrąg", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()