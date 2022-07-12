import cv2
import mediapipe as mp
import time


class handDetector():
    def __init__(self, mode=False,
               maxHands=2, model_complexity=1,
               detectionConfidence=0.5,trackingConfidence=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.model_complexity = model_complexity
        self.detectionConfidence = detectionConfidence
        self.trackingConfidence = trackingConfidence

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,
                                        self.detectionConfidence, self.trackingConfidence)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,
                                               self.mpHands.HAND_CONNECTIONS)
        return img
            # for id, lm in enumerate(handLms.landmark):
                # h, w, c = img.shape
                # cx, cy = int(lm.x * w), int(lm.y * h)
                # print("id: " + str(id) + ";     position: x = " + str(cx) + ", y = " + str(cy) + ";")
                # if id == 0:
                #     cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)


def main():
    cTime = 0  # initialising current & previous time = 0
    pTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        success, img = cap.read()
        img = detector.findHands(img)

        cTime = time.time() # current time
        fps = 1/(cTime-pTime) #calculate refresh rate ie. how fast the while loop runs
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN,
                    3, (255,0,255), 3)
        # the image, the text, position, font, font scale, color, thickness

        cv2.imshow("Image", img) #display image (window name, image variable)
        cv2.waitKey(1) #display window for "1" milisec, or till user quit


if __name__ == "__main__":
    main()















# Copied Code
# import cv2
# import mediapipe as mp
# import time
# class handDetector():
#     def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
#         self.mode = mode
#         self.maxHands = maxHands
#         self.detectionCon = detectionCon
#         self.trackCon = trackCon
#         self.mpHands = mp.solutions.hands
#         self.hands = self.mpHands.Hands(self.mode, self.maxHands,
#                                         self.detectionCon, self.trackCon)
#         self.mpDraw = mp.solutions.drawing_utils
#     def findHands(self, img, draw=True):
#         imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         self.results = self.hands.process(imgRGB)
#         # print(results.multi_hand_landmarks)
#         if self.results.multi_hand_landmarks:
#             for handLms in self.results.multi_hand_landmarks:
#                 if draw:
#                     self.mpDraw.draw_landmarks(img, handLms,
#                                                self.mpHands.HAND_CONNECTIONS)
#         return img
#     def findPosition(self, img, handNo=0, draw=True):
#         lmList = []
#         if self.results.multi_hand_landmarks:
#             myHand = self.results.multi_hand_landmarks[handNo]
#             for id, lm in enumerate(myHand.landmark):
#                 # print(id, lm)
#                 h, w, c = img.shape
#                 cx, cy = int(lm.x * w), int(lm.y * h)
#                 # print(id, cx, cy)
#                 lmList.append([id, cx, cy])
#                 if draw:
#                     cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
#         return lmList
# def main():
#     pTime = 0
#     cTime = 0
#     cap = cv2.VideoCapture(1)
#     detector = handDetector()
#     while True:
#         success, img = cap.read()
#         img = detector.findHands(img)
#         lmList = detector.findPosition(img)
#         if len(lmList) != 0:
#             print(lmList[4])
#         cTime = time.time()
#         fps = 1 / (cTime - pTime)
#         pTime = cTime
#         cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
#                     (255, 0, 255), 3)
#         cv2.imshow("Image", img)
#         cv2.waitKey(1)
# if __name__ == "__main__":
#     main()