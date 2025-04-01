import cv2
import numpy as np
import os
from ultralytics import YOLO


class YOLOv8Detector:
    def __init__(self, model_path, conf=0.5, iou=0.5):
        # 初始化模型
        self.model = YOLO(model_path)
        self.model.fuse()
        self.conf = conf
        self.iou = iou

        # 固定颜色生成（按类别ID）
        np.random.seed(42)  # 固定随机种子确保颜色一致
        self.COLORS = np.random.uniform(0, 255, size=(80, 3))

    def detect(self, img_source):
        """执行检测并返回带标注的图像和统计信息"""
        # 执行推理
        results = self.model.predict(
            source=img_source,
            imgsz=640,
            conf=self.conf,
            iou=self.iou,
            device='cpu',
            verbose=False
        )
        return self._parse_results(img_source.copy(), results[0])

    def _parse_results(self, img, results):
        """解析结果并绘制检测框"""
        statistic_dic = {}
        boxes = results.boxes.cpu().numpy()

        # 获取所有类别名称
        class_names = results.names.values()
        statistic_dic = {name: 0 for name in class_names}

        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cls_id = int(box.cls[0])
            conf = box.conf[0]
            class_name = results.names[cls_id]

            # 统计计数
            statistic_dic[class_name] += 1

            # 绘制检测框和标签
            color = self.COLORS[cls_id % len(self.COLORS)].tolist()
            label = f"{class_name} {conf:.2f}"

            # 绘制边框（加粗）
            cv2.rectangle(img, (x1, y1), (x2, y2), color, thickness=3)

            # 计算标签背景尺寸
            (text_w, text_h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)

            # 绘制标签背景
            cv2.rectangle(img,
                          (x1, y1 - text_h - 10),
                          (x1 + text_w, y1 - 10),
                          color,
                          -1)

            # 绘制文字
            cv2.putText(img, label,
                        (x1, y1 - 15),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (255, 255, 255),  # 白色文字
                        2)

        print("[检测统计]")
        for cls, count in statistic_dic.items():
            if count > 0:
                print(f"  {cls}: {count}个")
        return img


def main():
    # 参数配置
    model_path = "best.pt"  # 模型路径
    input_source = "123.png"  # 输入源：图片路径/视频路径/摄像头ID
    output_dir = "results"  # 输出目录

    # 窗口尺寸配置
    window_width = 800  # 窗口宽度
    window_height = 600  # 窗口高度

    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    # 初始化检测器
    detector = YOLOv8Detector(model_path, conf=0.5, iou=0.5)

    # 处理输入源
    if input_source.isdigit():
        # 摄像头模式
        cap = cv2.VideoCapture(int(input_source))
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS) or 30  # 默认30fps
        output_path = os.path.join(output_dir, "camera_output.mp4")
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))
    else:
        # 尝试作为图片打开
        img = cv2.imread(input_source)
        if img is not None:
            detected_img = detector.detect(img)
            # 保存图片结果
            filename = os.path.basename(input_source)
            output_path = os.path.join(output_dir, f"detected_{filename}")
            cv2.imwrite(output_path, detected_img)
            print(f"结果已保存至: {output_path}")

            # 显示结果
            cv2.namedWindow("YOLOv8 Detection", cv2.WINDOW_NORMAL)
            cv2.resizeWindow("YOLOv8 Detection", window_width, window_height)
            cv2.imshow("YOLOv8 Detection", detected_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            return
        else:
            # 视频文件模式
            cap = cv2.VideoCapture(input_source)
            frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = cap.get(cv2.CAP_PROP_FPS)
            # 创建输出路径
            filename = os.path.basename(input_source)
            output_path = os.path.join(output_dir, f"detected_{filename}")
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    # 视频/摄像头模式
    cv2.namedWindow("YOLOv8 Detection", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("YOLOv8 Detection", window_width, window_height)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # 执行检测
        detected_frame = detector.detect(frame)

        # 保存视频帧
        out.write(detected_frame)

        # 显示结果
        cv2.imshow("YOLOv8 Detection", detected_frame)

        # 退出条件
        if cv2.waitKey(1) & 0xFF in [ord('q'), 27]:  # 按Q或ESC退出
            break

    # 释放资源
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print(f"视频结果已保存至: {output_path}")


if __name__ == "__main__":
    main()