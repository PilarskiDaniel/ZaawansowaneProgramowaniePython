import cv2
import numpy as np

image = cv2.imread("konon.jpg")
if image is None:
    print("Błąd wczytywania obrazu")
    exit()

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

if len(faces) == 0:
    print("Nie wykryto twarzy")
    exit()

mask = np.zeros(image.shape[:2], dtype="uint8")

for (x, y, w, h) in faces:
    cv2.rectangle(mask, (x, y), (x+w, y+h), 255, -1)
    break

masked = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Original Image", image)
#cv2.imshow("Mask", mask)
cv2.imshow("Masked Face", masked)

cv2.waitKey(0)
cv2.destroyAllWindows()