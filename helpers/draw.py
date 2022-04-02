import cv2 as cv
import numpy as np

def line(path):
    # read the image
    img = cv.imread(path)
    # draw the line
    # (where to draw, (starting point), (ending point), (color), thickness)
    cv.line(img, (0,0), (200, 200), (0, 255, 0), 2) # (width, height)
    # display to user
    cv.imshow("Original image", img) # name of the output window + image to display
    cv.waitKey(0) # delay closing image output window to see the picture (ms, but 0 is infinite)