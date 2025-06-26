import cv2

image = cv2.imread('pies.jpg')

if image is None:
    print("Nie udało się wczytać obrazu.")
    exit()

(h, w) = image.shape[:2]
if h > 200 and w > 200:
    (b1, g1, r1) = image[50, 50]
    (b2, g2, r2) = image[200, 200]

    print("Pixel (50, 50) - R: {}, G: {}, B: {}".format(r1, g1, b1))
    print("Pixel (200, 200) - R: {}, G: {}, B: {}".format(r2, g2, b2))

    if (b1, g1, r1) == (b2, g2, r2):
        print("Wartości pikseli są identyczne.")
    else:
        print("Wartości pikseli są różne.")
else:
    print("Obraz jest zbyt mały, aby porównać piksele w punktach (50, 50) i (200, 200).")