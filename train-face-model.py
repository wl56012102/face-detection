import cv2,os
import numpy as np
from PIL import Image

cascadePath = "../data/haarcascades/haarcascade_profileface.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
recognizer = cv2.face.createLBPHFaceRecognizer()

def get_images_and_labels():
    images=[]
    labels=[]
    image_paths = [os.path.join('../data/face-data',f) for f in os.listdir('../data/face-data')]
    for image_path in image_paths:
        image_pil=Image.open(image_path).convert('L')
        image = np.array(image_pil,'uint8')
        images.append(image)
        labels.append(int('1'))
        cv2.imshow('add face',image)
        cv2.waitKey(50)
    return images,labels

if __name__ == '__main__':
    images,labels = get_images_and_labels()
    recognizer.train(images,np.array(labels))
    recognizer.save('model.yaml')
    #image_paths = [os.path.join('../data/face-data', f) for f in os.listdir('../data/face-data')]
    #for image_path in image_paths:
      #  predict_image_pil = Image.open(image_path).convert('L')
     #   predict_image = np.array(predict_image_pil,'uint8')
      #  a,b = recognizer.predict(predict_image)
     #   print(a,b)


