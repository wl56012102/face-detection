from flask import Flask, render_template, Response
import cv2
import time

class VideoCamera(object):
    def __init__(self):
        # 通过opencv获取实时视频流
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
        # 因为opencv读取的图片并非jpeg格式，因此要用motion JPEG模式需要先将图片转码成jpg格式图片
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()


app = Flask(__name__)


@app.route('/')  # 主页
def index():
    # jinja2模板，具体格式保存在index.html文件中
    return render_template('index.html',time="asd")


def gen(camera):
    while True:
        #frame = camera.get_frame()
        ret,frame= cv2.imread('./1.jpg')
        ret,jpeg = cv2.imencode('.jpg',frame)
        frame=jpeg.tobytes()
        # 使用generator函数输出视频流， 每次请求输出的content类型是image/jpeg
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')  # 这个地址返回视频流响应
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video')  # 这个地址返回视频流响应
def video():
    return Response("/static/1.mp4",
                    mimetype='text/plain')

@app.route('/get_time')
def get_time():
    return Response("asd",mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port = 5000)
    frame = gen(VideoCamera(0))