import cv2
import numpy as np

canvas_size = 300
triangle = np.zeros((canvas_size, canvas_size), dtype="uint8")
circle = np.zeros((canvas_size, canvas_size), dtype="uint8")

def draw_triangle(img, top_point):
    pts = np.array([
        top_point,
        (top_point[0] - 100, top_point[1] + 150),
        (top_point[0] + 100, top_point[1] + 150)
    ])
    cv2.fillPoly(img, [pts], 255)

draw_triangle(triangle, (150, 50))

cv2.circle(circle, (150, 150), 100, 255, -1)

cv2.imshow("Triangle", triangle)
cv2.imshow("Circle", circle)

bitwise_and = cv2.bitwise_and(triangle, circle)
bitwise_or = cv2.bitwise_or(triangle, circle)
bitwise_xor = cv2.bitwise_xor(triangle, circle)
bitwise_not_triangle = cv2.bitwise_not(triangle)

cv2.imshow("AND", bitwise_and)
cv2.imshow("OR", bitwise_or)
cv2.imshow("XOR", bitwise_xor)
cv2.imshow("NOT (Triangle)", bitwise_not_triangle)

cv2.waitKey(0)

triangle_moved = np.zeros((canvas_size, canvas_size), dtype="uint8")
draw_triangle(triangle_moved, (100, 50))  # przesunięty w lewo

cv2.imshow("Triangle Moved", triangle_moved)

bitwise_and_moved = cv2.bitwise_and(triangle_moved, circle)
bitwise_or_moved = cv2.bitwise_or(triangle_moved, circle)
bitwise_xor_moved = cv2.bitwise_xor(triangle_moved, circle)

cv2.imshow("AND Moved", bitwise_and_moved)
cv2.imshow("OR Moved", bitwise_or_moved)
cv2.imshow("XOR Moved", bitwise_xor_moved)

cv2.waitKey(0)
cv2.destroyAllWindows()