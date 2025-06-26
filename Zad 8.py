import cv2

image = cv2.imread("bomba.jpg")

if image is None:
    print("Nie można wczytać obrazu!")
    exit()

(h, w) = image.shape[:2]

roi_width = 200

x = 0

while True:
    if x + roi_width > w:
        break

    roi = image[0:h, x:x + roi_width]

    cv2.imshow("Przesuwany ROI - Naciśnij klawisz (q = wyjście)", roi)

    key = cv2.waitKey(0) & 0xFF

    if key == ord('q'):
        break

    x += 10

cv2.destroyAllWindows()