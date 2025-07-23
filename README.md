# 🎯 Smart Video Player with YOLOv5 Object Detection

The Smart Video Player with YOLOv5 Object Detection is an intelligent, real-time video analysis system designed to enhance surveillance, monitoring, and video stream resilience. Leveraging the powerful YOLOv5 deep learning model, this project performs fast and accurate object detection across video frames, supporting 80 object classes trained on the COCO dataset. What sets it apart is its built-in fault tolerance—when a stream fails or frame reading encounters issues, the system automatically retries connection attempts up to three times without manual intervention. It also features frame-by-frame logging with precise timestamps and overlaying of frame numbers on the video feed for detailed monitoring. To simulate robustness under stress, the script can deliberately trigger frame read failures at a predefined frame, testing the system’s recovery capability in controlled environments. The entire detection process is thoroughly logged, making this project ideal for developers, researchers, and engineers looking to integrate advanced, resilient AI-driven video processing into their applications.

---

## 🔍 YOLOv5 Model Setup

```python
from ultralytics import YOLO

model = YOLO('yolov5s.pt')
```

- 🧠 **Trained on**: COCO dataset  
- 🎯 **Detects**: 80 object classes  
- ⚡ **Fast and lightweight** (ideal for real-time)

---

## ⚙️ Configuration (`main.py`)

```python
VIDEO_SOURCE = "video1.mp4"         # Path to your video file or stream
RECONNECT_TRIES = 3                 # Max retry attempts on failure
ENABLE_FAILURE_SIMULATION = True    # Toggle frame read failure simulation
simulate_failure_at = 100           # Frame number to simulate failure
```

---

## ▶️ How to Run

### 1. 📦 Install dependencies

```bash
pip install -r requirements.txt
```

### 2. 🎥 Place your video file

Put `video1.mp4` in the root directory.

### 3. 🚀 Run the detection script

```bash
python main.py
```

Press `q` to quit. Logs will be saved in the `logs/` directory.

---

## 📋 Requirements

Dependencies listed in `requirements.txt`:

```text
torch
torchvision
ultralytics
opencv-python
numpy
```

Install them using:

```bash
pip install -r requirements.txt
```

---

## 🧪 Failure Simulation

To test system resilience, enable in `main.py`:

```python
ENABLE_FAILURE_SIMULATION = True
simulate_failure_at = 100
```

Triggers a simulated failure at frame 100 and auto-reconnects to validate fault tolerance.

---

## 📝 Logging System

- `logs/detections.log`: Logs stream status, reconnections, frame reads, and detections with timestamps and elapsed time.
- `logs/detection_log.txt`: Logs object detections with confidence and labels from `utils.py`.

---

## 📊 Console Output Example

```log
[INFO] Attempting to open video source... (Try 1/3)
[INFO] Stream started successfully.
[INFO] Processing frame 1
...
[SIMULATION] Simulating frame read failure at frame 100.
[WARNING] Frame read failed. Attempting to reconnect...
[INFO] Stream started successfully.
[INFO] Processing frame 101
...
```

---

## 🎬 Video Output Preview

- ✅ Objects enclosed in bounding boxes with labels and confidence
- 🔢 Frame count shown on top-left
- 🔁 "Reconnecting..." overlay during stream failure

Preview available in the `sample_output/` folder.

---

## 💡 Contributions & License

Pull requests are welcome! Improve detection logic, add GUI features, or integrate alert systems.

📄 **Licensed under the MIT License**

Built using 💻 Python, 🧠 YOLOv5, and 🧪 fault-tolerant design principles.
<img width="1812" height="1029" alt="image" src="https://github.com/user-attachments/assets/71bac811-db0b-4a9a-8006-036c7d9e7038" />

<img width="969" height="581" alt="image" src="https://github.com/user-attachments/assets/d0c2c537-7c9e-466c-83dd-438c03fd2e6a" />

