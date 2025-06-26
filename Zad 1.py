import cv2

image = cv2.imread("bb.jpg")
cv2.imshow("Oryginalny obraz", image)

flipped = cv2.flip(image, 1)
cv2.imshow("Odbicie poziome", flipped)

cv2.waitKey(0)
cv2.destroyAllWindows()