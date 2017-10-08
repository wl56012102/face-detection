import cv2
import os
import sys
import numpy as np
from PIL import Image
import imutils
import argparse

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
    a=recognizer.train(images,np.array(labels))
    print(a)


