import cv2
import imutils


def find_and_draw_contours(image, thresh):
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    output = image.copy()
    cv2.drawContours(output, contours, -1, (0, 0, 255), 2)
    return output, len(contours)


def main():
    image = cv2.imread("kostka.jpg")
    if image is None:
        print("Nie udało się wczytać obrazu. Sprawdź ścieżkę.")
        return

    widths = [600, 400, 300, 150]

    for w in widths:
        resized = imutils.resize(image, width=w)
        gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)

        output, count = find_and_draw_contours(resized, thresh)

        print(f"Rozdzielczość: {w}px szerokości - wykryto konturów: {count}")

        cv2.imshow(f'Kontury przy szerokości {w}px', output)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()