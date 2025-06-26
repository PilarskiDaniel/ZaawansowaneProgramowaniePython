import cv2
img1 = cv2.imread('example.jpg')
img2 = cv2.imread('grey.jpg')
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey(0)
#można zamknąć te zdjęcia niezależnie klikając w "X"