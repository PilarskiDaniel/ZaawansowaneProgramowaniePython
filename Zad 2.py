import cv2
import imutils
import numpy as np


def find_and_draw_contours(image, thresh, mode, mode_name):
    contours, hierarchy = cv2.findContours(thresh.copy(), mode, cv2.CHAIN_APPROX_SIMPLE)

    output = image.copy()

    cv2.drawContours(output, contours, -1, (0, 0, 255), 2)

    cv2.imshow(f'Kontury - tryb {mode_name} - liczba konturów: {len(contours)}', output)

    return len(contours), hierarchy


def main():
    image = cv2.imread("kostka.jpg")
    if image is None:
        print("Nie udało się wczytać obrazu. Sprawdź ścieżkę do pliku.")
        return

    resized = imutils.resize(image, width=300)

    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)

    cv2.imshow('Obraz progowany', thresh)

    modes = [
        (cv2.RETR_EXTERNAL, 'RETR_EXTERNAL'),
        (cv2.RETR_LIST, 'RETR_LIST'),
        (cv2.RETR_TREE, 'RETR_TREE')
    ]

    for mode, mode_name in modes:
        count, hierarchy = find_and_draw_contours(resized, thresh, mode, mode_name)

        print(f"Tryb {mode_name} wykrył {count} konturów.")
        if mode == cv2.RETR_EXTERNAL:
            print("RETR_EXTERNAL - zwraca tylko zewnętrzne kontury (najbardziej zewnętrzne obiekty).")
        elif mode == cv2.RETR_LIST:
            print("RETR_LIST - zwraca wszystkie kontury bez hierarchii (lista konturów).")
        elif mode == cv2.RETR_TREE:
            print("RETR_TREE - zwraca wszystkie kontury i hierarchię (relacje rodzic-dziecko).")

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()