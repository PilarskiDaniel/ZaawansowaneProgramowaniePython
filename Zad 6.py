import cv2

image = cv2.imread("fq.jpg")
(h, w) = image.shape[:2]

roi = image[0:100, 0:100]

if h >= 100 and w >= 100:
    image[h-100:h, w-100:w] = roi
else:
    print("Obraz jest za mały, by wkleić ROI w prawym dolnym rogu.")

cv2.imshow("Obraz po wklejeniu fragmentu", image)
cv2.waitKey(0)
cv2.destroyAllWindows()