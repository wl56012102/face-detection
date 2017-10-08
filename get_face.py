import cv2

def get_face(img):
    face_cascade = cv2.CascadeClassifier('./data/haarcascades/haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    return faces


if __name__ == '__main__':
    face_cascade = cv2.CascadeClassifier('./data/haarcascades/haarcascade_frontalface_default.xml')
    camera = cv2.VideoCapture(0)
    face_count = 0
    file_name=input('input object name:')
    while True:
        ret, img = camera.read()
        faces = get_face(img)
        print(faces)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_color = img[y:y + h, x:x + w]
            face_count += 1
            face_name = './data/face-data/' + file_name +"."+str(face_count) + '.jpg'
            roi_color=cv2.resize(roi_color,(200,200))
            cv2.imwrite(face_name, roi_color)
        cv2.imshow("frame", img)
        key = cv2.waitKey(5) & 0xff
        if key == ord("q"):
            break
        if face_count>=100:
            break
    camera.release()
    cv2.destroyAllWindows()
