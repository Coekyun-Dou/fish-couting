from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('runs/train/exp/weights/best.pt') # 自己训练结束后的模型权重
    model.val(data='dataset/data.yaml',
              split='val',
              imgsz=640,
              batch=16,
              save_json=True, # if you need to cal coco metrice
              project='runs/val',
              name='exp',
              )
