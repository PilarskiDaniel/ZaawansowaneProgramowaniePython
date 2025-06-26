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
        cx = x + w // 2
        cy = y + h // 2

        mask = np.zeros(image.shape[:2], dtype="uint8")
        cv2.drawContours(mask, [c], -1, 255, -1)
        segmented_brick = cv2.bitwise_and(image, image, mask=mask)
        roi = segmented_brick[y:y+h, x:x+w]

        filename = f"kostka_{i:02d}.png"
        cv2.imwrite(filename, roi)

        cv2.drawContours(output, [c], -1, (0, 255, 0), 2)
        cv2.putText(output, str(i), (cx - 10, cy), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 2)

    cv2.imshow("Numerowane kostki", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()