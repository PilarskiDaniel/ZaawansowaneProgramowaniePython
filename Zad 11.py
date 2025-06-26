import cv2
import numpy as np

image = cv2.imread('pies.jpg')

if image is None:
    print("Nie udało się wczytać obrazu.")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)

print("Najjaśniejszy piksel:")
print("Współrzędne: (x={}, y={})".format(maxLoc[0], maxLoc[1]))
print("Wartość jasności (0–255):", int(maxVal))

cv2.circle(image, maxLoc, 5, (0, 0, 255), 2)
cv2.imshow("Najjaśniejszy piksel", image)
cv2.waitKey(0)
cv2.destroyAllWindows()