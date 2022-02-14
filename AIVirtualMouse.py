import cv2
import time
import HandTrackingModule as htm

cap = cv2.VideoCapture(0)
detector = htm.HandDetector(min_detection_confidence=0.75)
pTime = 0

while True:
    success, img = cap.read(0)
    img = detector.findHands(img)
    lmList = detector.findLocation(img, draw=False)

    if len(lmList) != 0:
        x8, y8 = lmList[8][1:]
        x12, y12 = lmList[12][1:]

        fingers = detector.findUpDownFingers()
        print(fingers)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    cv2.imshow('AI Virtual Mouse', img)
    cv2.waitKey(1)
