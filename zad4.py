import cv2
image = cv2.imread("grey.jpg")
newImage = cv2.imwrite("new.jpg", image) #zapis nowego pliku    