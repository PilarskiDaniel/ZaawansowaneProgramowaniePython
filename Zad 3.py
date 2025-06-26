import cv2

image = cv2.imread("delmito.jpg")
cv2.imshow("Original", image)

new_width = 200
new_height = 300
dim = (new_width, new_height)

resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

cv2.imshow("Resized 200x300", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()