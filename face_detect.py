import os
import cv2

def get_face(img):
    face_cascade = cv2.CascadeClassifier('./data/haarcascades/haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    return faces

if __name__ == '__main__':
    cascadePath = "./data/haarcascades/haarcascade_profileface.xml"
    image_paths = [os.path.join('./data/face-data', f) for f in os.listdir('./data/face-data')]
    faceCascade = cv2.CascadeClassifier(cascadePath)
    recognizer = cv2.face.createLBPHFaceRecognizer()
    recognizer.load('model.yaml')
    face_name=''
    camera = cv2.VideoCapture(0)
    while True:
        ret ,img = camera.read()
        faces = get_face(img)
        for (x, y, w, h) in faces:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            roi_gray= gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]
            a,b = recognizer.predict(roi_gray)
            if(int(b)>75):
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                face_name='unknow'
                cv2.putText(img, face_name, (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 0, 255), 1)
            else:
                for image_path in image_paths:
                    if (os.path.split(image_path)[1].split('.')[0] == str(a)):
                        face_name=os.path.split(image_path)[1].split('.')[1]
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.putText(img,str(a)+" "+face_name+" "+str(int(b)),(x,y-20),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),1)
        cv2.imshow("frame", img)
        key = cv2.waitKey(5)&0xff
        if key ==ord("q"):
            break
    camera.release()
    cv2.destroyAllWindows()