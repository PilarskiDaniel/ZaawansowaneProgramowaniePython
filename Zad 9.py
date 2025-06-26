import cv2

image = cv2.imread("fq.jpg")

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()

cropped = image[0:300, 0:300]

cv2.imshow("Cropped 300x300", cropped)

cv2.imwrite("cropped_image.jpg", cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()