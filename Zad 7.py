import cv2

image = cv2.imread("bomba.jpg")
(h, w) = image.shape[:2]

cell_height = h // 3
cell_width = w // 3

cells = []

for row in range(3):
    for col in range(3):
        y_start = row * cell_height
        y_end = (row + 1) * cell_height
        x_start = col * cell_width
        x_end = (col + 1) * cell_width
        cell = image[y_start:y_end, x_start:x_end]
        cells.append(cell)

for idx, part in enumerate(cells):
    cv2.imshow(f"Czesc {idx+1}", part)

cv2.waitKey(0)
cv2.destroyAllWindows()