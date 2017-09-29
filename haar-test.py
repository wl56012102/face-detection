import cv2
import numpy as np

def get_face(img):
    face_cascade = cv2.CascadeClassifier('./data/haarcascades/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('./data/haarcascades/haarcascade_eye.xml')


if __name__ == '__main__':

    camera = cv2.VideoCapture(0)
    face_count=0
    while True:
        ret ,img = camera.read()
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        print(faces)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            face_count+=1
            face_name='./data/face-data/'+'wanglei'+str(face_count)+'.jpg'
            cv2.imwrite(face_name,roi_color)
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        cv2.imshow("gray",gray)
        cv2.imshow("frame",img)
        key = cv2.waitKey(5)&0xff
        if key ==ord("q"):
            break
    camera.release()
    cv2.destroyAllWindows()
    