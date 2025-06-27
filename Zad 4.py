import cv2

image = cv2.imread('pies.jpg')
(h, w) = image.shape[:2]
print(f"Wymiary obrazu: szerokość = {w}, wysokość = {h}")

x = int(input("Podaj współrzędną X: "))
y = int(input("Podaj współrzędną Y: "))

if 0 <= x < w and 0 <= y < h:
    # Ustawienie koloru na czarny
    image[y, x] = (0, 0, 0)
    print(f"Zmieniono piksel na pozycji ({x}, {y}) na czarny.")
    cv2.imshow("Zmodyfikowany obraz", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Błąd: podane współrzędne wykraczają poza rozmiar obrazu.")
