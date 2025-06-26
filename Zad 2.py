import cv2

image = cv2.imread("bb.jpg")
cv2.imshow("Oryginalny obraz", image)

flipped_vert = cv2.flip(image, 0)
cv2.imshow("Odbicie pionowe", flipped_vert)

cv2.waitKey(0)
cv2.destroyAllWindows()