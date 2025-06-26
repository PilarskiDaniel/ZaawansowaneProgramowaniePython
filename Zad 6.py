import cv2

print("Wybierz sposób odbicia:")
print("0 - odbicie pionowe")
print("1 - odbicie poziome")
print("-1 - odbicie względem obu osi")
flip_code = int(input("Podaj wartość (0, 1 lub -1): "))

image = cv2.imread("bb.jpg")
cv2.imshow("Oryginał", image)

if flip_code not in [0, 1, -1]:
    print("Niepoprawny wybór! Używam odbicia poziomego (1) domyślnie.")
    flip_code = 1

flipped = cv2.flip(image, flip_code)

cv2.imshow("Obrócony obraz", flipped)
cv2.waitKey(0)
cv2.destroyAllWindows()