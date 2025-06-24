from ultralytics import YOLO
import cv2

class DebrisDetector:
    def __init__(self, model_path='yolov8n.pt'):
        self.model = YOLO(model_path)
    
    def detect(self, image_path):
        """Détection des débris sur une image"""
        img = cv2.imread(image_path)
        results = self.model.predict(img)
        return [
            {
                'position': [int(box.xyxy[0][0]), int(box.xyxy[0][1])],
                'confidence': box.conf.item()
            }
            for box in results[0].boxes
        ]