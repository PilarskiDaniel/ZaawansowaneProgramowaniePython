import cv2

image = cv2.imread("profilowe.jpg")
if image is None:
    print("Nie udało się wczytać obrazu.")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
mouth_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

for (x, y, w, h) in faces:
    center = (x + w // 2, y + h // 2)
    radius = max(w, h) // 2
    cv2.circle(image, center, radius, (255, 0, 0), 3)

    # Obszar twarzy do dalszej detekcji
    roi_gray = gray[y:y + h, x:x + w]
    roi_color = image[y:y + h, x:x + w]

    # Detekcja oczu
    eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=8)
    for (ex, ey, ew, eh) in eyes[:2]:  # tylko 2 oczy
        eye_center = (x + ex + ew // 2, y + ey + eh // 2)
        eye_radius = int((ew + eh) * 0.25)
        cv2.circle(image, eye_center, eye_radius, (0, 0, 255), -1)

    # Detekcja ust
    mouths = mouth_cascade.detectMultiScale(roi_gray, scaleFactor=1.7, minNeighbors=20)
    for (mx, my, mw, mh) in mouths:
        if my > h // 2:
            cv2.rectangle(image,
                          (x + mx, y + my),
                          (x + mx + mw, y + my + mh),
                          (0, 255, 0), -1)
            break
cv2.imshow("Zamaskowana twarz", image)
cv2.waitKey(0)
cv2.destroyAllWindows()