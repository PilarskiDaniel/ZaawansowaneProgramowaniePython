import cv2

image = cv2.imread("delmito.jpg")
cv2.imshow("Original", image)

new_width = image.shape[1] * 4
new_height = image.shape[0] * 4

# Powiększenie z użyciem INTER_CUBIC
resized_cubic = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_CUBIC)
cv2.imshow("INTER_CUBIC", resized_cubic)
cv2.waitKey(0)

# Powiększenie z użyciem INTER_LANCZOS4
resized_lanczos = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LANCZOS4)
cv2.imshow("INTER_LANCZOS4", resized_lanczos)
cv2.waitKey(0)

cv2.destroyAllWindows()