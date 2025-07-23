# 🎯 Smart Video Player with YOLOv5 Object Detection

A real-time object detection system using **YOLOv5** with smart recovery features, timestamped logs, and failure simulation support.

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
