import cv2

image = cv2.imread("jumper.jpg")
cv2.imshow("Oryginalny obraz", image)

(h, w) = image.shape[:2]

center = (0, 0)

M = cv2.getRotationMatrix2D(center, 30, 1.0)

rotated = cv2.warpAffine(image, M, (w, h))

cv2.imshow("Obrócony o 30 stopni wokół narożnika", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()