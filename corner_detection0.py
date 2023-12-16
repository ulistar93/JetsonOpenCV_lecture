import cv2
import numpy as np

src = cv2.imread("SuperMoon.png")
dst = src.copy()
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 5, blockSize=3, userHarrisDetector=True, k=0.03)

for x, y in corners:
    cv2.circle(dst, (x, y), 3, (0, 0, 255), 2)

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()