import cv2

angle = float(input("Podaj kąt obrotu (w stopniach): "))

image = cv2.imread("jumper.jpg")
cv2.imshow("Oryginalny obraz", image)

(h, w) = image.shape[:2]
center = (w // 2, h // 2)

M = cv2.getRotationMatrix2D(center, angle, 1.0)

rotated = cv2.warpAffine(image, M, (w, h))

cv2.imshow(f"Obrócony o {angle} stopni", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()