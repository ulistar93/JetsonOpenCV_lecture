import numpy as np
import cv2
import time


def perf(func):
    def wrapper(*args, **kwargs):
        e1 = time.perf_counter()
        func(*args, **kwargs)
        e2 = time.perf_counter()
        print("py time: ", e2 - e1)
    return wrapper

@perf
def func1(img):
    res = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

@perf
def func2(img):
    res = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# img = cv2.imread("starry_night.jpg")
img = cv2.imread("bright.jpg")
func1(img)
func2(img)