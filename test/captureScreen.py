import cv2
import mss
import numpy as np

# 定义全局变量
drawing = False  # 是否正在绘制矩形框
ix, iy = -1, -1  # 矩形框左上角的坐标
x, y = -1, -1  # 矩形框右下角的坐screenshot
screenshot=np.zeros((1280, 720, 3), np.uint8)
def draw_rectangle(event, _x, _y, flags, param):
    global ix, iy, x, y, drawing,screenshot
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = _x, _y
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        x, y = _x, _y
        cv2.rectangle(screenshot, (ix, iy), (x, y), (0, 255, 0), 2)

        # 计算矩形框的坐标和大小
        x, y = max(ix, x), max(iy, y)
        width, height = abs(ix - x), abs(iy - y)

        print("矩形框的坐标和大小：({}, {}) - {} x {}".format(ix, iy, width, height))
        cv2.imshow("screenshot", screenshot)


def boxScreen(screenshot1):
    global ix, iy, x, y, drawing,width, height,screenshot
    screenshot=screenshot1
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2RGB)
    # 显示截图在 OpenCV 窗口中
    cv2.imshow("screenshot", screenshot)
    cv2.setMouseCallback('screenshot', draw_rectangle)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return ix, iy, x, y


if __name__ == "__main__":
    x0, y0, x1, y1 = boxScreen()
    print(x0, y0, x1, y1)
