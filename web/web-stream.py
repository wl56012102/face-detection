from flask import Flask, render_template, Response
import cv2
import time

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_face(self,image):
        face_cascade = cv2.CascadeClassifier('../data/haarcascades/haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        return faces

    def get_frame(self):
        success, image = self.video.read()
        faces = self.get_face(image)
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        cv2.putText(image, str(now), (10, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        for(x,y,w,h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_color = image[y:y + h, x:x + w]
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()


app = Flask(__name__)


@app.route('/')  # 主页
def index():
    return render_template('index.html')


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video')
def video():
    return Response("/static/1.mp4",
                    mimetype='text/plain')

@app.route('/get_time')
def get_time():
    return Response("asd",mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port = 5000,processes=5)
