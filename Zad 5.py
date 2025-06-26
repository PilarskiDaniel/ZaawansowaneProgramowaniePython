import cv2

image = cv2.imread("fq.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

if len(faces) == 0:
    print("Nie wykryto żadnej twarzy.")
else:
    (x, y, w, h) = faces[0]
    face_roi = image[y:y+h, x:x+w]

    cv2.imshow("Wykryta twarz", face_roi)
    cv2.waitKey(0)
    cv2.destroyAllWindows()