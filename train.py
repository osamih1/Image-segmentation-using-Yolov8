from ultralytics import YOLO

# loading the pretrained model
model = YOLO("yolov8n-seg.pt")

# training the model for 1 epoch
model.train(data="config.yaml", epochs=10)