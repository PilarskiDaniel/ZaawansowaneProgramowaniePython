import cv2

image = cv2.imread("win.jpg")

B, G, R = cv2.split(image)

cv2.imshow("Original Image", image)
cv2.imshow("Blue Channel", B)
cv2.imshow("Green Channel", G)
cv2.imshow("Red Channel", R)

print("Sprawdź na ekranie, które obiekty są najbardziej wyraźne w poszczególnych kanałach.")

cv2.waitKey(0)
cv2.destroyAllWindows()