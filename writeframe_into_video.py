import cv2
import glob
import os

def img2vid(imgs_dir, save_name):
    fps = 30 # 30/sec
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video_writer = cv2.VideoWriter(save_name, fourcc, fps, (500, 300))
    imgs = glob.glob(os.path.join(imgs_dir, '*.jpg'))

    for i in range(len(imgs)):
        imgname = os.path.join(imgs_dir, '%d.jpg' % i)
        print("process... ",imgname)
        frame = cv2.imread(imgname)
        video_writer.write(frame)
    video_writer.release()


# 路徑要記得改
imgs_dir="D:/qiongyun/desktop/project/content_img/"
# 圖片資料夾檔案名：0.jpg, 1.jpg, 2.png,......
save_name="new_video".avi"
imgvid(imgs_dir,save_name)
