import cv2

image = cv2.imread("jumper.jpg")
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

M = cv2.getRotationMatrix2D((cX, cY), 75, 1.0)

rotated = cv2.warpAffine(image, M, (w, h))

cv2.imwrite("rotated_output.jpg", rotated)

cv2.imshow("Rotated Image", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()