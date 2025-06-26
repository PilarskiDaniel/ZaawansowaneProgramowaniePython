import cv2
import imutils

image = cv2.imread("testo.jpg")
cv2.imshow("Oryginalny obraz", image)

translated = imutils.translate(image, 100, 50)

cv2.imshow("Przesunięcie imutils.translate", translated)
cv2.waitKey(0)
cv2.destroyAllWindows()

#zauważalnych różnic nie widzę, jedynie to łatwiej się go stosuje w porównaniu do cv2.warpAffine