import cv2

logo = cv2.imread("opcv.jpg")

B, G, R = cv2.split(logo)

swapped = cv2.merge([R, G, B])

no_green = cv2.merge([B, 0 * G, R])

cv2.imshow("Original Logo", logo)
cv2.imshow("Swapped B and R", swapped)
cv2.imshow("No Green Channel", no_green)

cv2.waitKey(0)
cv2.destroyAllWindows()