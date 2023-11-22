# version 0.0.1

import cv2

def capture_video():
    cap = cv2.VideoCapture(0)  # Capture video from the first webcam
    while True:
        ret, frame = cap.read()
        if ret:
            # Process the frame (resize, encode, etc.)
            yield frame
    cap.release()
