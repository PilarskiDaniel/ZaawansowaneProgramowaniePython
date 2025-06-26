import cv2

image = cv2.imread("jumper.jpg")
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

for angle in range(0, 361, 15):
    M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))

    cv2.imshow("Rotacja", rotated)
    key = cv2.waitKey(500)

    if key != -1:
        break

cv2.destroyAllWindows()