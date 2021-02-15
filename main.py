import cv2 as cv
import numpy as np
import pyautogui

cap = cv.VideoCapture(0)

yellow_lower = np.array([22,93,0])
yellow_upper = np.array([45,255,255])

prev_y = 0

while True:
    ret, frame = cap.read()
    #Creating Mask of Video
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, yellow_lower, yellow_upper)

    # Finding Contours
    contours, hier = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    # filtering the contours
    for contour in contours:
        area = cv.contourArea(contour)
        if area > 1000:
            x, y, w, z = cv.boundingRect(contour)
            cv.rectangle(frame, (x, y), (x+w,y+z), (0,255,0), 5)
            if y < prev_y:
                pyautogui.press('space')
                print('Down')
            prev_y = y

    cv.imshow("Live Video", frame)
    # cv.imshow("Mask Video", mask)

    if cv.waitKey(10)==ord('q'):
        break

cap.release()
cv.destroyAllWindows()