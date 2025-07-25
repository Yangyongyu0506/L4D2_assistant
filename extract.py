import cv2
import os

def extract_frames(video_path, output_dir, interval=5):
    """
    从视频中每隔 interval 帧提取一帧保存为图片
    """
    os.makedirs(output_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    frame_id = 0
    saved_id = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if frame_id % interval == 0:
            filename = os.path.join(output_dir, f"frame_{saved_id:05d}.jpg")
            cv2.imwrite(filename, frame)
            saved_id += 1

        frame_id += 1

    cap.release()
    print(f"提取完成，共保存 {saved_id} 张图片到 {output_dir}")

# 用法
if __name__ == "__main__":
    extract_frames("C:\\Users\\86132\\Desktop\\Academics\\Python\\Yolo\\l4d2\\sourcedata.mp4", "C:\\Users\\86132\\Desktop\\Academics\\Python\\Yolo\\l4d2\\dataset", interval=5)
