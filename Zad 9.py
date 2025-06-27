import cv2

image = cv2.imread('pies.jpg')

before = image.copy()

(h, w) = image.shape[:2]
if h > 100 and w > 100:
    image[50:100, 50:100] = (255, 255, 255)

    cv2.imshow("Przed zmianą", before)
    cv2.imshow("Po zmianie (obszar 50–100 na biało)", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Obraz jest zbyt mały – nie można zastosować zmian w podanym obszarze.")