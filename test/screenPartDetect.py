import mss
import cv2 as CV2
import os
import threading
import time
import torch
import numpy as np

from test.captureScreen import boxScreen

yolov5 = torch.hub.load('F:\\science_study\\sea_win_eletronic_detect\\lab\yolov5\\yolov5-CBAM-Wise-IoU', 'custom',
                        path='C:\\Users\\jw\Desktop\\sea_wind_eletron_defect_detect_system\\pt\\yolov5CW.pt',
                        device='0', source='local')
yolov5.conf = 0.3
yolov5.iou = 0.4

COLORS = [
    (0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), (0, 255, 255),
    (255, 0, 255), (192, 192, 192), (128, 128, 128), (128, 0, 0),
    (128, 128, 0), (0, 128, 0)]

LABELS = ['', 'erosion', 'crack', 'sandhole']
img_src = np.zeros((1280, 720, 3), np.uint8)


def getScreenshot():
    mtop, mbot = 30, 50
    monitor = {"left": x0, "top": y0, "width": x1 - x0, "height": y1 - y0}
    img_src = np.array(mss.mss().grab(monitor))
    time.sleep(0.1)
    img_src = img_src[:, :, :3]
    img_src = img_src[mtop:-mbot]
    return img_src, [x0, y0, x1, y1, mtop, mbot]


def getMonitor():
    global img_src
    while True:
        img_src, _ = getScreenshot()


def yolov5Detect():
    CV2.namedWindow("detectWindow", CV2.WINDOW_NORMAL)
    CV2.resizeWindow("detectWindow", x1-x0, y1-y0)
    CV2.moveWindow("detectWindow", 600, 600)
    global img_src
    while True:
        img = img_src.copy()
        bboxes = getDetection(img)
        img = drawBBox(img, bboxes)
        CV2.imshow("detectWindow", img)
        if CV2.waitKey(1) & 0xFF == ord("q"):
            # 就会销毁窗口并退出循环，否则继续下一次循环。
            CV2.destroyAllWindows()
            os._exit(0)



def getLargestBox(bboxes, type):
    largest = -1
    bbox_largest = np.array([])
    for bbox in bboxes:
        if LABELS[int(bbox[5])] in type:
            x0, y0, x1, y1 = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
            area = (x1 - x0) * (y1 - y0)
            if area > largest:
                largest = area
                bbox_largest = bbox
    return bbox_largest


def drawBBox(image, bboxes):
    for bbox in bboxes:
        conf = bbox[4]
        classID = int(bbox[5])
        if conf > yolov5.conf:
            x0, y0, x1, y1 = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
            if classID >= 10:
                classID = 10
            color = [int(c) for c in COLORS[classID]]
            CV2.rectangle(image, (x0, y0), (x1, y1), color, 3)
            text = "{}: {:.2f}".format(LABELS[classID], conf)
            CV2.putText(image, text, (max(0, x0), max(0, y0 - 5)), CV2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
            print([x0, y0, x1, y1], text)
    return image


def getDetection(img):
    bboxes = np.array(yolov5(img[:, :, ::-1], size=1280).xyxy[0].cpu())
    return bboxes


def srceendetect():
    global x0, y0, x1, y1
    x0, y0, x1, y1 = boxScreen()
    print(x0, y0, x1, y1)
    t1 = threading.Thread(target=getMonitor, args=())
    t1.start()
    t2 = threading.Thread(target=yolov5Detect, args=())
    t2.start()

if __name__ == "__main__":
    srceendetect();