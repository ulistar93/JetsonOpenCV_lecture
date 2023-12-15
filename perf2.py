import numpy as np
import cv2

max_count = 100
def func():
    cap = cv2.VideoCapture("vtest.avi")
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret or count >= max_count:
            break
        count += 1
        
def func2():
    cap = cv2.VideoCapture("vtest.avi")
    count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        cv2.resize(frame,(640,480), interpolation=cv2.INTER_CUBIC)
        if not ret or count >= max_count:
            break
        count += 1

# e1 = cv2.getTickCount()
# func()
# e2 = cv2.getTickCount()
# print("cv time: ", (e2 - e1)/ cv2.getTickFrequency() )

import time
e1 = time.perf_counter()
func()
e2 = time.perf_counter()
print("cap.set: ", e2 - e1)

import time
e1 = time.perf_counter()
func2()
e2 = time.perf_counter()
print("resize: ", e2 - e1)