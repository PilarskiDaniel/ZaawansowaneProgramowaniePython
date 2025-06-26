import cv2
import numpy as np

image = cv2.imread("konon.jpg")
if image is None:
    print("Błąd wczytywania obrazu")
    exit()

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])

mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask = cv2.bitwise_or(mask1, mask2)

mask_inv = cv2.bitwise_not(mask)

darkened = cv2.bitwise_and(image, image, mask=mask)
background = cv2.bitwise_and(image, image, mask=mask_inv)
background = cv2.convertScaleAbs(background, alpha=0.3, beta=0)

result = cv2.add(darkened, background)

cv2.imshow("Original", image)
cv2.imshow("Mask", mask)
cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()