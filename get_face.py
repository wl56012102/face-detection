import cv2
import os


def get_face(img):
    face_cascade = cv2.CascadeClassifier('./data/haarcascades/haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    return faces


if __name__ == '__main__':
    face_cascade = cv2.CascadeClassifier('./data/haarcascades/haarcascade_frontalface_default.xml')
    camera = cv2.VideoCapture(0)
    face_count = 0
    face_id=input('input face id:')
    face_name=input('input face name:')
    image_paths = [os.path.join('./data/face-data', f) for f in os.listdir('./data/face-data')]
    for image_path in image_paths:
        if(os.path.split(image_path)[1].split('.')[0]==face_id):
            os.remove(image_path)
    while True:
        ret, img = camera.read()
        faces = get_face(img)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_color = img[y:y + h, x:x + w]
            face_count += 1
            file_name = './data/face-data/' + face_id+"."+face_name +"."+str(face_count) + '.jpg'
            roi_color=cv2.resize(roi_color,(200,200))
            cv2.imwrite(file_name, roi_color)
        cv2.putText(img,str(face_count),(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
        cv2.imshow("frame", img)
        key = cv2.waitKey(5) & 0xff
        if key == ord("q"):
            break
        if face_count>=200:
            break
    camera.release()
    cv2.destroyAllWindows()
