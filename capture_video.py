# version 0.1.1

import cv2
from flask import Flask, Response

def capture_video():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if ret:
            # Convert the captured frame to JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            # Convert to bytes and yield
            frame = buffer.tobytes()
            # Using a multipart format for streaming
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        else:
            break
    cap.release()

# Set up Flask app
app = Flask(__name__)

@app.route('/video_feed')
def video_feed():
    return Response(capture_video(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
