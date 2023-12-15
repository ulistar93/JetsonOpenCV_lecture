import numpy as np
import cv2

def func():
    img1 = cv2.imread("messi5.jpg")
    for i in range(5,49,2):
        img1 = cv2.medianBlur(img1,i)

e1 = cv2.getTickCount()
func()
e2 = cv2.getTickCount()
print("cv time: ", (e2 - e1)/ cv2.getTickFrequency() )

import time
e1 = time.perf_counter()
func()
e2 = time.perf_counter()
print("py time: ", e2 - e1)