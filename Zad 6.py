import cv2

image = cv2.imread('pies.jpg')
(h, w) = image.shape[:2]

center_x = w // 2
center_y = h // 2

half_size = 50

start_x = center_x - half_size
end_x = center_x + half_size
start_y = center_y - half_size
end_y = center_y + half_size

start_x = max(0, start_x)
end_x = min(w, end_x)
start_y = max(0, start_y)
end_y = min(h, end_y)

image[start_y:end_y, start_x:end_x] = (0, 0, 255)

cv2.imshow("Kwadrat czerwony na środku", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
