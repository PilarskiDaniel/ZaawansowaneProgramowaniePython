import cv2

image = cv2.imread('pies.jpg')
(h, w) = image.shape[:2]
cX, cY = w // 2, h // 2
print(f"Środek obrazu: x = {cX}, y = {cY}")

(b, g, r) = image[cY, cX]
print("Pixel at center ({}, {}) - Red: {}, Green: {}, Blue: {}".format(cX, cY, r, g, b))
