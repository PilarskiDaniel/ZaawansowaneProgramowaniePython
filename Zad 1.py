import cv2

image = cv2.imread("bomba.jpg")

roi = image[0:100, 0:100]

cv2.imshow("ROI - lewy górny róg 100x100", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()