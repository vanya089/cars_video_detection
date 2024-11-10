# src/detect_video.py
import os
import cv2
from yolov5 import detect
from IPython.display import Video

def detect_objects_on_video(video_path):
    if not os.path.exists(video_path):
        print(f"Video file not found: {video_path}")
        return

    frame_width, frame_height = 676, 380  # размеры для модели YOLO

    detect.run(weights="yolov5s.pt",
               source=video_path,
               conf_thres=0.4,
               imgsz=(frame_width, frame_height), 
               project="./output_detection", 
               name="video_detection",  
               exist_ok=True)

if __name__ == "__main__":
    video_path = "./video.mp4"  # Путь к видеофайлу
    detect_objects_on_video(video_path)
    Video("./output_detection/video_detection/video.mp4", embed=True)
