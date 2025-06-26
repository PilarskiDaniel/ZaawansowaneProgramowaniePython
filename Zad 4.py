import cv2

image = cv2.imread("bb.jpg")

flip_horizontal = cv2.flip(image, 1)

flip_vertical = cv2.flip(image, 0)

flip_both = cv2.flip(image, -1)

cv2.imshow("Oryginalny", image)
cv2.imshow("Odbicie poziome", flip_horizontal)
cv2.imshow("Odbicie pionowe", flip_vertical)
cv2.imshow("Odbicie względem obu osi", flip_both)

cv2.waitKey(0)
cv2.destroyAllWindows()