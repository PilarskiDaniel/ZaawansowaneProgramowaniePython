import cv2

image = cv2.imread("bb.jpg")
cv2.imshow("Oryginalny obraz", image)

flipped_both = cv2.flip(image, -1)
cv2.imshow("Odbicie względem obu osi", flipped_both)

cv2.waitKey(0)
cv2.destroyAllWindows()