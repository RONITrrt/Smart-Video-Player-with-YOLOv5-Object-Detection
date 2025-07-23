import cv2
from ultralytics import YOLO
from datetime import datetime
import time
import os

# === CONFIG ===
VIDEO_SOURCE = "video2.mp4"  # Replace with your IP stream or file path
RECONNECT_TRIES = 3
LOG_PATH = "logs/detections.log"

# === Load YOLOv5s Model ===
print("[INFO] Loading YOLOv5s model...")
model = YOLO('yolov5s.pt')  # Downloads if not available

# === Logging Setup ===
os.makedirs("logs", exist_ok=True)
log_file = open(LOG_PATH, "w")
start_time = time.time()  

def log_event(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    elapsed = time.time() - start_time
    log_file.write(f"[{timestamp}] (Elapsed: {elapsed:.2f}s) {message}\n")
    log_file.flush()

# === Video Reader with Retry Mechanism ===
def start_stream():
    retries = 0
    while retries < RECONNECT_TRIES:
        print(f"[INFO] Attempting to open video source... (Try {retries+1}/{RECONNECT_TRIES})")
        cap = cv2.VideoCapture(VIDEO_SOURCE)

        if cap.isOpened():
            print("[INFO] Stream started successfully.")
            log_event("Video stream started successfully.")
            return cap

        print(f"[WARNING] Cannot open video source. Retrying...")
        log_event("Video source open failed.")
        retries += 1
        time.sleep(2)

    print("[ERROR] Failed to open video source after 3 retries.")
    log_event("Failed to open video source after multiple attempts.")
    return None

# === Start Stream Initially ===
cap = start_stream()
if cap is None:
    exit()

# === Failure Simulation Toggle ===
ENABLE_FAILURE_SIMULATION = True  # Set to False to disable simulation
simulate_failure_at = 100  # Simulate failure at this frame number
frame_counter = 0  # Frame counter for simulation

# === Main Detection Loop ===
while cap.isOpened():
    success, frame = cap.read()
    frame_counter += 1

    # === Simulated Failure Section ===
    if ENABLE_FAILURE_SIMULATION and frame_counter == simulate_failure_at:
        print(f"[SIMULATION] Simulating frame read failure at frame {frame_counter}.")
        log_event(f"Simulated frame read failure at frame {frame_counter}.")
        success = False

    if not success:
        print("[WARNING] Frame read failed. Attempting to reconnect...")
        log_event("Frame read failed. Attempting reconnection...")

        # Display reconnecting on screen
        if 'frame' in locals() and frame is not None:
            reconnecting_frame = frame.copy()
            cv2.putText(reconnecting_frame, "Reconnecting...", (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 0, 255), 3)
            cv2.imshow("Smart Video Player - Object Detection", reconnecting_frame)
            cv2.waitKey(500)

        cap.release()
        cap = start_stream()

        if cap is None:
            print("[ERROR] Exiting due to repeated failure to reconnect.")
            log_event("Exiting due to repeated failure to reconnect.")
            break
        continue

    # === YOLO Detection ===
    results = model(frame)[0]
    for box in results.boxes:
        cls_id = int(box.cls[0])
        label = model.names[cls_id]
        conf = float(box.conf[0])
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        log_event(f"Detected: {label} with confidence {conf:.2f}")

    # === Show Frame Number on Video ===
    cv2.putText(frame, f"Frame: {frame_counter}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

    # === Print & Log Frame Count ===
    print(f"[INFO] Processing frame {frame_counter}")
    log_event(f"Processing frame {frame_counter}")

    cv2.imshow("Smart Video Player - Object Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("[INFO] Quit signal received. Exiting.")
        log_event("Quit signal received. Exiting.")
        break

# === Cleanup ===
cap.release()
log_file.close()
cv2.destroyAllWindows()
