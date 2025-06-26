import cv2
import imutils

image = cv2.imread("delmito.jpg")
cv2.imshow("Original", image)

methods = [
    ("INTER_AREA", cv2.INTER_AREA),
    ("INTER_NEAREST", cv2.INTER_NEAREST),
    ("INTER_LINEAR", cv2.INTER_LINEAR),
    ("INTER_CUBIC", cv2.INTER_CUBIC),
    ("INTER_LANCZOS4", cv2.INTER_LANCZOS4)
]

new_width = image.shape[1] // 5
new_height = image.shape[0] // 5

for (name, method) in methods:
    resized = cv2.resize(image, (new_width, new_height), interpolation=method)
    cv2.imshow(f"Method: {name}", resized)
    cv2.waitKey(0)

cv2.destroyAllWindows()