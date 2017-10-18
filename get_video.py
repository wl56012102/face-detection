import cv2
from imutils.video import VideoStream
import imutils


def main():
    camera = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'X264')
    vs =VideoStream()
    cv2.dnn.

    while True:
        ret, frame = camera.read()
        cv2.imshow("frame", frame)
        frame = cv2.flip(frame, 1)
        out.write(frame)

        key = cv2.waitKey(5) & 0xff
        if key == ord("q"):
            break
    camera.release()
    out.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
