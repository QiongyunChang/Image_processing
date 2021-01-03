'''
黑轉白白轉黑
'''
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
import sys

save_root = "D:/qiongyun/desktop/result/"
u2net = "D:/qiongyun/desktop/u2net_results/"

def segmentation(fname_ori):
    save_path = save_root+ os.path.split(fname_ori)[1]
    # predic_dir
    fname = u2net + os.path.split(fname_ori)[1].split('.')[0]+ '.png'
    # print(fname)
    image = plt.imread(fname)
    original = plt.imread(fname_ori)
    img = image.copy()
    for c in range(3):
        img[:,:,c] = np.where(image[:,:,c]>=0.5,255,0)
    img = np.array(img,np.int32)
    ROI = np.where(img != 0, original,0)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(ROI)

    image_show = cv2.cvtColor(ROI, cv2.COLOR_RGB2BGR)
    cv2.imwrite(save_path, image_show)
    # plt.show()

root_path = "D:/qiongyun/desktop/project/content_img/"
files = os.listdir(root_path)
for file in files:
    file_path = os.path.join(root_path,file)
    # print(file_path)
    segmentation(file_path)
