from ultralytics import YOLO
import torch

def main():
    model = YOLO('yolov8n.pt')  # 或 yolov8s.pt 等
    model.train(
        data='data/data.yaml',
        epochs=50,
        imgsz=1088,
        batch=8,
        name='left4dead2_yolov8n',
        device=0 if torch.cuda.is_available() else 'cpu',  # 使用 GPU
        #device = {True: 0, False: 'cpu'}[torch.cuda.is_available()],  # 使用 GPU
    )

if __name__ == '__main__':
    import multiprocessing
    multiprocessing.freeze_support()  # 可选，加上更保险
    main()