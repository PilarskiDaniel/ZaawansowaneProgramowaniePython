import cv2
cv2.namedWindow("output", cv2.WINDOW_NORMAL)
im = cv2.imread("example.jpg")
cv2.imshow("output", im)
cv2.waitKey(0)