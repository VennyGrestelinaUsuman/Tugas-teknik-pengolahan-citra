import numpy as np
import cv2

img = cv2.imread('lena.jpg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
_,thresh2 = cv2.threshold(gray,120, 255, cv2.THRESH_BINARY_INV)

cv2.imshow('Picture', thresh)
cv2.waitKey(0)
cv2. destroyAllWindows()