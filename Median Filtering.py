import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('venny.jpg')
blur = cv2.medianBlur(img,5)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blured')
plt.xticks([]),plt.yticks([])
plt.show()