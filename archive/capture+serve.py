# version 0.1.0

import cv2
from flask import Flask, Response

# Define capture_video function
def capture_video():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if ret:
            # Process the frame (resize, encode, etc.)
            yield frame
    cap.release()

# Set up Flask app
app = Flask(__name__)

@app.route('/video_feed')
def video_feed():
    return Response(capture_video(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
