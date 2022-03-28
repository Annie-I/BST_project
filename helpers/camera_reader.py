from sre_constants import SUCCESS
import cv2 as cv

def stream():
    input = cv.VideoCapture(0, cv.CAP_DSHOW) # 0 to use default camera or provide id
    # set window size / properties:
    input.set(3, 640) # defining width
    input.set(4, 480) # defining height
    input.set(10, 100) # change brightness

    # as video is a sequence of pictures, display them one after another:
    while True:
        # try to save image in img variable. success == true if loaded.
        SUCCESS, img = input.read()
        # img delay + option to break out of loop:
        cv.imshow("video", img)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cv.destroyAllWindows()