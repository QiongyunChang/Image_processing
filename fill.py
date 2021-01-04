'''
一張張填入把黑的部分用另一張圖填滿
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


'''
整個資料夾丟入
'''
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
# (segment 後的圖)
img_path = "D:/qiongyun/desktop/"
# (style transfer後的圖)要貼上的部分
imgpaste_path = "D:/qiongyun/desktop/paste"
# 轉出來後要存入的地方
save_path  = "D:/qiongyun/desktop/paste"
for i in range(283):
    img = plt.imread(os.path.join(img_path,"%d.jpg"%i))
    #style transfer圖
    img = plt.imread(os.path.join(imgpaste_path, "%d.png" % i))
    img_p = cv2.resize(img_p,(500,300))
    # plt.imshow(img_p)
    # plt.show()
    img1 = img.copy()
    p = img.copy()
    gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    x, y = np.where(gray[:, :] <= 10)
    p[x,y] = img_p[x,y]*255
    cv2.imwrite(os.path.join(save_path,"%d.jpg"% i), p)
    plt.imshow(p)
    plt.show()
