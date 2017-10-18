import cv2
from imutils.video import VideoStream
import imutils
import time

def main():
    camera = cv2.VideoCapture(0)
    vs =VideoStream(0).start()
    time.sleep(2)
    fourcc = cv2.VideoWriter_fourcc(*"MJPG")
    writer=None
    writer = cv2.VideoWriter('output.avi', fourcc, 15, (640, 480), 1)
    while True:
        ret, frame = camera.read()

        frame = cv2.flip(frame, 1)
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        cv2.putText(frame, str(now), (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        output =frame
        writer.write(output)
        cv2.imshow("frame", frame)
        key = cv2.waitKey(5) & 0xff
        if key == ord("q"):
            break
    camera.release()
    vs.stop()
    writer.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
