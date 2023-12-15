import cv2
import sys

img = cv2.imread("starry_night.jpg")
if img is None:
    sys.exit("Could not read the image.")

height, width, channel = img.shape
print(height, width , channel)

cv2.imshow("Display window", img)

k = cv2.waitKey()

if k == ord ('s'):
    cv2.imwrite("starry_night22.png", img)
cv2.destroyAllWindows()
