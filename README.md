Smart Video Player with YOLOv5 Object Detection
This project is a smart video monitoring system that uses YOLOv5 for real-time object detection. It includes:

Automatic retry mechanism for failed video streams.

Frame-by-frame detection with logs.

Frame failure simulation for testing robustness.

Frame counter with overlay on video.

Timestamped logging of events and detections.

🛠️ Features
✅ Real-time object detection using YOLOv5s
✅ Automatic reconnection (up to 3 times) if stream fails
✅ Detection logs with timestamps and elapsed time
✅ Frame number overlay on video feed
✅ Simulated failure at specific frame for robustness testing
✅ User can quit at any time with ctrl+c

📁 Project Structure
├── main.py             # Main video processing and YOLO detection
├── utils.py            # Helper for drawing boxes and logging detections
├── requirements.txt    # All required dependencies
├── yolov5su.pt          # YOLOv5s model (auto-downloaded if not present)
└── logs/
    ├── detections.log      # Frame-by-frame events and detections
🔧 Requirements
You can install all dependencies using:
pip install -r requirements.txt
requirements.txt includes:
torch
torchvision
ultralytics
opencv-python
numpy
▶️ How to Run
Place your video file (e.g., video1.mp4) in the same directory.

Run the script:
python main.py
Watch the console and video window:
Press q to quit

Logs will be saved in logs/

🔍 YOLOv5 Model
This project uses the ultralytics version of YOLOv5:

from ultralytics import YOLO
model = YOLO('yolov5s.pt')
The model will be automatically downloaded the first time you run the script if not already present.

⚙️ Configuration
Inside main.py:
VIDEO_SOURCE = "video1.mp4"       # Path to your video file or stream
RECONNECT_TRIES = 3               # Max retry attempts on failure
ENABLE_FAILURE_SIMULATION = True  # Toggle simulated frame failure
simulate_failure_at = 100         # Frame at which to simulate failure
🧪 Failure Simulation
To test the robustness of the video stream, set:
ENABLE_FAILURE_SIMULATION = True
simulate_failure_at = 100
At frame 100, the video will simulate a failure. The app will then try to reconnect up to 3 times.

📝 Logs
logs/detections.log: Logs frame-by-frame events (stream opened, failures, detections) with timestamp and elapsed time.

logs/detection_log.txt: Logs all detected objects (from utils.py) with timestamp and confidence.

📌 Example Console Output
[INFO] Attempting to open video source... (Try 1/3)
[INFO] Stream started successfully.
[INFO] Processing frame 1
[INFO] Processing frame 2
...
[SIMULATION] Simulating frame read failure at frame 100.
[WARNING] Frame read failed. Attempting to reconnect...
[INFO] Stream started successfully.
[INFO] Processing frame 101
...
#sample_output 
In sample_output file there are videos and sample of detection that thr model made

🎥 Video Output Preview
Bounding boxes are drawn for detected objects.

Frame number is displayed at the top-left corner.

A red "Reconnecting..." overlay appears if stream fails temporarily.
