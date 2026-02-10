# app.py
from flask import Flask, render_template, Response, jsonify
import cv2
from face_recognition import recognize_face

app = Flask(__name__)
camera = cv2.VideoCapture(0)

def gen_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            faces = recognize_face(frame)
            for face in faces:
                x, y, w, h = face['box']
                if face['status'] == "PRESENT":
                    color = (0, 255, 0)
                else:
                    color = (0, 0, 255)
                cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
                cv2.putText(frame, f"{face['name']} {face['status']}", (x, y-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

            ret, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/attendance')
def attendance():
    # Read CSV and return data as JSON
    data = []
    try:
        with open("attendance.csv", "r") as f:
            for line in f.readlines():
                name, time = line.strip().split(',')
                data.append({"name": name, "time": time})
    except:
        pass
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
