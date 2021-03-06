import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('bnw.jpg',0)
ret, thresh = cv2.threshold(img,127, 225, cv2.THRESH_BINARY)
kernel = np.ones((5,5),np.uint8)
erosi = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel)

plt.subplot(131),plt.imshow(img,cmap='gray')
plt.title('Citra Awal'),plt.xticks([]),plt.yticks([])
plt.subplot(132),plt.imshow(thresh,cmap='gray')
plt.title('Citra Biner'), plt.xticks([]),plt.yticks([])
plt.subplot(132),plt.imshow(erosi,cmap='gray')
plt.title('Hasil Opening'),plt.xticks([]),plt.yticks([])

plt.show()