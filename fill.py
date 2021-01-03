'''
把黑的部分用另一張圖填滿
'''
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import cv2
img = plt.imread("D:/qiongyun/desktop/145.jpg")
img_p = plt.imread("D:/qiongyun/desktop/145.png")
img_p = cv2.resize(img_p,(500,300))
# plt.imshow(img_p)
# plt.show()
img1 = img.copy()
p = img.copy()
gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
x, y = np.where(gray[:, :] <= 10)
p[x,y] = img_p[x,y]*255
print(x,y)
print(np.shape(x),np.shape(y))
plt.imshow(p)
plt.show()
