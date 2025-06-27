import cv2

image = cv2.imread('pies.jpg')

before = image.copy()

if image.shape[0] > 100:
    image[100, :] = (0, 255, 0)

    cv2.imshow("Przed zmianą", before)
    cv2.imshow("Po zmianie (100. wiersz = zielony)", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Obraz ma mniej niż 101 wierszy – nie można zmienić 100. wiersza.")