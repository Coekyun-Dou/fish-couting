from ultralytics import YOLO

# Load a model
model = YOLO("../../v8/yolov8n.yaml")  # yaml文件可根据需求更改
#model = YOLO("yolov8n.pt")  #  不使用预训练权重，就注释这一行即可
# train
model.train(data="../../testdata/data.yaml",
                cache=False,
                imgsz=640,
                epochs=100,
                batch=16,
                close_mosaic=0,
                workers=4,
                optimizer='SGD', # using SGD
                project='runs',
                name='exp'
                )

