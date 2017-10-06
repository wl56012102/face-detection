import cv2

def main():
    camera = cv2.VideoCapture(0)
    while True:
        ret ,frame = camera.read()
        cv2.imshow("frame",frame)
        key = cv2.waitKey(5)&0xff
        if key ==ord("q"):
            break
    camera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
    