import cv2

image = cv2.imread("delmito.jpg")
cv2.imshow("Original", image)

new_width = image.shape[1] * 2
new_height = image.shape[0] * 2
dim = (new_width, new_height)

resized = cv2.resize(image, dim, interpolation=cv2.INTER_LINEAR)

cv2.imshow("Resized - double size", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()