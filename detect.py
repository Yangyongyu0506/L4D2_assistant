from ultralytics import YOLO

class YoloDetector:
    def __init__(self, model_path=r'C:\Users\86132\Desktop\Academics\Python\YOLO\l4d2\runs\detect\left4dead2_yolov8n7\weights\best.pt'):
        self.model = YOLO(model_path)

    def detect(self, frame):
        results = self.model.predict(source=frame, conf=0.4, verbose=False)
        return results[0]  # 带坐标的预测对象
