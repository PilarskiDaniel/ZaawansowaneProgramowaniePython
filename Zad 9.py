import cv2

image = cv2.imread("delmito.jpg")
cv2.imshow("Original", image)

original_height, original_width = image.shape[:2]

for scale in [x / 100 for x in range(100, 301, 20)]:
    # Oblicz nowe wymiary
    new_width = int(original_width * scale)
    new_height = int(original_height * scale)

    resized = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

    cv2.imshow(f"Scale: {int(scale * 100)}%", resized)
    key = cv2.waitKey(500)

    if key == ord('q'):
        break

cv2.destroyAllWindows()