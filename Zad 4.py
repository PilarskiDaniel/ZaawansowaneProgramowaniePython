import cv2

image = cv2.imread("bomba.jpg")
(h, w) = image.shape[:2]

print(f"Wymiary obrazu: szerokość={w}, wysokość={h}")

startX = int(input(f"Podaj startX (0 - {w-1}): "))
endX = int(input(f"Podaj endX ({startX+1} - {w}): "))
startY = int(input(f"Podaj startY (0 - {h-1}): "))
endY = int(input(f"Podaj endY ({startY+1} - {h}): "))

if startX < 0 or endX > w or startX >= endX:
    print("Niepoprawne wartości X.")
    exit()
if startY < 0 or endY > h or startY >= endY:
    print("Niepoprawne wartości Y.")
    exit()

roi = image[startY:endY, startX:endX]

cv2.imshow("Wybrany ROI", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()