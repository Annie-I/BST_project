from sre_constants import SUCCESS
import cv2 as cv

def play(path):
    vid = cv.VideoCapture(path) # create video capture object

    # as video is a sequence of pictures, display them one after another:
    while True:
        SUCCESS, img = vid.read() # try to save image in img variable. success == true if loaded.
        cv.imshow("video", img)
        # img delay + option to break out of loop:
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cv.destroyAllWindows()