import numpy as np
import cv2

canvas = np.zeros((400, 400, 3), dtype="uint8")

green = (0, 255, 0)
red = (0, 0, 255)

top_left_green = (0, 0)
bottom_right_green = (100, 50)
cv2.rectangle(canvas, top_left_green, bottom_right_green, green, -1)  # -1 oznacza wypełnienie

top_left_red = (400 - 100, 400 - 50)
bottom_right_red = (399, 399)
cv2.rectangle(canvas, top_left_red, bottom_right_red, red, 3)

cv2.imshow("Prostokąty", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()