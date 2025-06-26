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

    for i, c in enumerate(contours, start=1):
        c = c.astype("float")
        c *= ratio
        c = c.astype("int")

        x, y, w, h = cv2.boundingRect(c)

        cv2.rectangle(output, (x, y), (x + w, y + h), (255, 0, 0), 2)

        text = f"{w}x{h} px"
        cv2.putText(output, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.6, (0, 0, 255), 2)

    cv2.imshow("Wymiary kostek", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()