import cv2
from cvzone.HandTrackingModule import HandDetector
import os

model = HandDetector()
cap=cv2.VideoCapture(0)
while True:   
    status,photo=cap.read()
    hand=model.findHands(photo)
    cv2.imshow("Gesture recognition",photo)
    if cv2.waitKey(100) ==13:
        break
    lmlist=hand[0]
#     print(lmlist)
    while len(lmlist)!=0:
        fingeruplist=model.fingersUp(lmlist[0])
        print(fingeruplist)
        if fingeruplist ==[1,0,0,0,0]:
            os.system("mspaint")
            break
        elif fingeruplist ==[0,1,0,0,0]:
            os.system("control panel")
            break
        elif fingeruplist ==[0,0,1,0,0]:
            print("Go to hell!!")
            break
        elif fingeruplist ==[0,0,0,1,0]:
            os.system("cmd")
            break
        elif fingeruplist ==[0,0,0,0,1]:
            os.system("notepad")
            break
        elif fingeruplist ==[1,1,1,1,1]:
            print("Hii! HOw are you ? ")
            break
        else:
            print("Unable to recognise!")
            break

cap.release()
cv2.destroyAllWindows()