import cv2
import imutils

def main():
    image = cv2.imread("kostka.jpg")
    if image is None:
        print("Nie udało się wczytać obrazu. Sprawdź ścieżkę do pliku.")
        return

    resized = imutils.resize(image, width=300)

    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

    threshold_values = [100, 140, 180]

    for thresh_val in threshold_values:
        _, thresh = cv2.threshold(gray, thresh_val, 255, cv2.THRESH_BINARY)
        cv2.imshow(f'Progowanie - wartość progu: {thresh_val}', thresh)

    cv2.imshow('Obraz oryginalny (przeskalowany)', resized)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()