import cv2
import os
from datetime import datetime

def draw_boxes(frame, detections):
    for _, row in detections.iterrows():
        label = row['name']
        conf = row['confidence']
        x1, y1, x2, y2 = map(int, [row['xmin'], row['ymin'], row['xmax'], row['ymax']])
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    return frame

def log_detection(detections):
    os.makedirs("logs", exist_ok=True)
    with open("logs/detection_log.txt", "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for _, row in detections.iterrows():
            f.write(f"[{timestamp}] Detected: {row['name']} ({row['confidence']:.2f})\n")
