import numpy as np
import cv2

r = 0.3
src = cv2.imread("coins.png")
src = cv2.resize(src, (0, 0), fx=r, fy=r)
number1 = np.ones_like(src) * 127
number2 = np.ones_like(src) * 2

add = cv2.add(src, number1)
sub = cv2.subtract(src, number1)
mul = cv2.multiply(src, number2)
div = cv2.divide(src, number2)
# add2 = src + number1
# sub2 = src - number1
# mul2 = src * number2
# div2 = src / number2
# add2 = src + 127
# sub2 = src - 127
# mul2 = src * 2
# div2 = src / 2
add2 = np.uint8(src + 127)
sub2 = np.uint8(src - 127)
mul2 = np.uint8(src * 2)
div2 = np.uint8(src / 2)

src = np.concatenate((src, src, src, src), axis=1)
number = np.concatenate((number1, number1, number2, number2), axis=1) 
dst = np.concatenate((add, sub, mul, div), axis=1)
dst2 = np.concatenate((add2, sub2, mul2, div2), axis=1)

# res = np.concatenate((src, number, dst), axis=0)
res = np.concatenate((src, number, dst, dst2), axis=0)

cv2.imshow("dst", res)
cv2.waitKey(0)
cv2.destroyAllWindows()