import cv2

image = cv2.imread('pies.jpg')
(h, w) = image.shape[:2]
print(f"Wymiary obrazu: wysokość = {h}, szerokość = {w}")

(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))