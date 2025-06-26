import cv2
# Wczytanie obrazu z pliku
image = cv2.imread("example.jpg")
cv2.imshow("Wyswietlony obraz", image) # Tworzy okno i wyświetla obraz
cv2.waitKey(0) # Czeka na dowolny klawisz, by zamknąć okno
cv2.destroyAllWindows() # Zamknięcie wszystkich okien
print(image)
# Sprawdzenie, czy obraz został poprawnie wczytany
if image is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    print("Obraz wczytano poprawnie.")