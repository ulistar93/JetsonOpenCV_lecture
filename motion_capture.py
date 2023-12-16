import cv2
import numpy as np
import matplotlib.pyplot as plt


width = 640
height = 480
fps = 30
device = "/dev/video0"
gst_str = f"v4l2src device={device} io-mode=2 \
	! image/jpeg, width=(int)320, height=(int)240, framerate=30/1 \
	! nvv4l2decoder mjpeg=1 ! nvvidconv ! video/x-raw,format=BGRx \
	! videoconvert ! video/x-raw, format=BGR ! appsink"


cap = cv2.VideoCapture(gst_str, cv2.CAP_GSTREAMER)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

frame_prev = ''
while True:
    ret, frame = cap.read()
    if not ret:
        break
    if frame_prev:
        diff = frame - freme_prev
        pass 
    if cv2.waitKey(33) == 27:
        break
    frame_prev = frame.copy()

cv2.destroyAllWindows()
