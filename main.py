import cv2
import mediapipe as mp
import numpy as np
import math

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

prev_x, prev_y = None, None

color = (255, 0, 255)
brush_thickness = 7
eraser = False
eraser_size = 45

canvas = np.zeros((480, 640, 3), dtype=np.uint8)

def distance(p1, p2, w, h):
    x1, y1 = int(p1.x * w), int(p1.y * h)
    x2, y2 = int(p2.x * w), int(p2.y * h)
    return math.hypot(x2 - x1, y2 - y1)

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    h, w, c = img.shape

    if canvas.shape[:2] != (h, w):
        canvas = np.zeros((h, w, 3), dtype=np.uint8)

    # Toolbar
    cv2.circle(img, (40, 40), 18, (0, 0, 255), -1)
    cv2.circle(img, (90, 40), 18, (0, 255, 0), -1)
    cv2.circle(img, (140, 40), 18, (255, 0, 0), -1)
    cv2.circle(img, (190, 40), 18, (0, 255, 255), -1)

    cv2.circle(img, (260, 40), 18, (255, 255, 255), -1)
    cv2.putText(img, "B", (252, 48), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

    cv2.circle(img, (310, 40), 18, (180, 180, 180), -1)
    cv2.putText(img, "E", (302, 48), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for hand in results.multi_hand_landmarks:
            lm = hand.landmark
            mp_draw.draw_landmarks(img, hand, mp_hands.HAND_CONNECTIONS)

            cx = int(lm[8].x * w)
            cy = int(lm[8].y * h)

            thumb_index_dist = distance(lm[4], lm[8], w, h)

            # Only draw when thumb and index are apart
            drawing_active = thumb_index_dist > 45

            # Cursor
            cv2.circle(img, (cx, cy), 10, color if not eraser else (180, 180, 180), -1)

            # Toolbar selection
            if cy < 80:
                if 20 < cx < 60:
                    color = (0, 0, 255)
                    eraser = False
                elif 70 < cx < 110:
                    color = (0, 255, 0)
                    eraser = False
                elif 120 < cx < 160:
                    color = (255, 0, 0)
                    eraser = False
                elif 170 < cx < 210:
                    color = (0, 255, 255)
                    eraser = False
                elif 240 < cx < 280:
                    eraser = False
                elif 290 < cx < 330:
                    eraser = True

                prev_x, prev_y = None, None

            elif drawing_active:
                if prev_x is not None and prev_y is not None:
                    cx = int(0.6 * prev_x + 0.4 * cx)
                    cy = int(0.6 * prev_y + 0.4 * cy)

                    if eraser:
                        cv2.circle(canvas, (cx, cy), eraser_size, (0, 0, 0), -1)
                    else:
                        cv2.line(canvas, (prev_x, prev_y), (cx, cy), color, brush_thickness)

                prev_x, prev_y = cx, cy

            else:
                prev_x, prev_y = None, None

    else:
        prev_x, prev_y = None, None

    output = cv2.add(img, canvas)
    cv2.imshow("Air Canvas", output)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()