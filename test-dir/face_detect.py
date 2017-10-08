import os
import cv2

def get_face(img):
    face_cascade = cv2.CascadeClassifier('../data/haarcascades/haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    return faces

if __name__ == '__main__':
    cascadePath = "../data/haarcascades/haarcascade_profileface.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)
    recognizer = cv2.face.createLBPHFaceRecognizer()
    recognizer.load('model.yaml')
    camera = cv2.VideoCapture(0)
    while True:
        ret ,img = camera.read()
        faces = get_face(img)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            roi_gray= gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]
            a,b = recognizer.predict(roi_gray)
            print(a,b)
        cv2.imshow("frame", img)
        key = cv2.waitKey(5)&0xff
        if key ==ord("q"):
            break
    camera.release()
    cv2.destroyAllWindows()