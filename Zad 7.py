import cv2

image = cv2.imread('pies.jpg')
(h, w) = image.shape[:2]

cell_w = w // 3
cell_h = h // 3

start_x = cell_w
end_x = cell_w * 2
start_y = cell_h
end_y = cell_h * 2

center_crop = image[start_y:end_y, start_x:end_x]

cv2.imshow("Środkowy fragment obrazu", center_crop)
cv2.waitKey(0)
cv2.destroyAllWindows()