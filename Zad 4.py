import cv2

image = cv2.imread("delmito.jpg")
cv2.imshow("Original", image)

scale = 3
new_width = image.shape[1] * scale
new_height = image.shape[0] * scale
dim = (new_width, new_height)

methods = [
    ("INTER_NEAREST", cv2.INTER_NEAREST),
    ("INTER_LINEAR", cv2.INTER_LINEAR),
    ("INTER_CUBIC", cv2.INTER_CUBIC),
    ("INTER_LANCZOS4", cv2.INTER_LANCZOS4)
]

for (name, method) in methods:
    resized = cv2.resize(image, dim, interpolation=method)
    cv2.imshow(f"Method: {name}", resized)
    print(f"[INFO] Wyświetlam obraz z interpolacją: {name}")
    cv2.waitKey(0)

cv2.destroyAllWindows()