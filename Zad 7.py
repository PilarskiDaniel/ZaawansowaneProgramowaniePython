import cv2
import imutils
import numpy as np

def main():
    image = cv2.imread("kostka.jpg")
    if image is None:
        print("Nie udało się wczytać obrazu.")
        return

    resized = imutils.resize(image, width=300)
    ratio = image.shape[0] / float(resized.shape[0])

    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    output = image.copy()

    min_area = 500
    max_area = 5000

    widths = []
    heights = []

    filtered_contours = []

    for c in contours:
        area = cv2.contourArea(c)
        if area < min_area or area > max_area:
            continue

        filtered_contours.append(c)

    for i, c in enumerate(filtered_contours, start=1):
        c = c.astype("float")
        c *= ratio
        c = c.astype("int")

        x, y, w, h = cv2.boundingRect(c)

        widths.append(w)
        heights.append(h)

        cv2.rectangle(output, (x, y), (x + w, y + h), (255, 0, 0), 2)
        text = f"{w}x{h} px"
        cv2.putText(output, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.6, (0, 0, 255), 2)

    cv2.imshow("Wymiary filtrowanych kostek", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    if len(filtered_contours) == 0:
        print("Nie wykryto kostek po filtracji.")
        return

    avg_width = sum(widths) / len(widths)
    avg_height = sum(heights) / len(heights)

    min_width = min(widths)
    max_width = max(widths)
    min_height = min(heights)
    max_height = max(heights)

    print("Raport wykrytych kostek:")
    print(f"Liczba kostek: {len(filtered_contours)}")
    print(f"Średnia szerokość: {avg_width:.2f} px")
    print(f"Średnia wysokość: {avg_height:.2f} px")
    print(f"Minimalna szerokość: {min_width} px")
    print(f"Maksymalna szerokość: {max_width} px")
    print(f"Minimalna wysokość: {min_height} px")
    print(f"Maksymalna wysokość: {max_height} px")

if __name__ == "__main__":
    main()