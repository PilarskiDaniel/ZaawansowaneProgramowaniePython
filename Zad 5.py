import cv2

image = cv2.imread("bb.jpg")

(h, w) = image.shape[:2]

start_x = w // 3
start_y = h // 3
end_x = start_x + w // 3
end_y = start_y + h // 3

roi = image[start_y:end_y, start_x:end_x]

flipped_roi = cv2.flip(roi, 1)

image[start_y:end_y, start_x:end_x] = flipped_roi

cv2.imshow("Fragment odbity poziomo", image)
cv2.waitKey(0)
cv2.destroyAllWindows()