import imp
from turtle import circle
import cv2 as cv
import numpy as np

# function to read picture and show to user
def displayAsIs(path):
    # read the image
    img = cv.imread(path)
    # print image size
    print(img.shape)
    # display to user
    cv.imshow("img", img) # name of the output window + image to display
    cv.waitKey(0) # delay closing image output window to see the picture (ms, but 0 is infinite)

    cv.destroyAllWindows()

# function to read picture, convert it to grayscale and show to user
def displayGrayscale(path):
    # read the image
    img = cv.imread(path)
    # convert to grayscale picture
    grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # display to user
    cv.imshow("gray img", grayImg) # name of the output window + image to display
    cv.waitKey(0) # delay closing image output window to see the picture (ms, but 0 is infinite)

    cv.destroyAllWindows()

# function to read picture, convert it to binary and show to user
def displayBinary(path):
    # read the image
    img = cv.imread(path)
    # convert to grayscale picture
    grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # transform to binary
    (thresh, binaryImage) = cv.threshold(grayImg, 127, 255, cv.THRESH_BINARY)
    # display to user
    cv.imshow("binary img", binaryImage) # name of the output window + image to display
    cv.waitKey(0) # delay closing image output window to see the picture (ms, but 0 is infinite)

    cv.destroyAllWindows()

# function to read picture, convert it to binary and save it to disc
def saveBinary(path):
    # read the image
    img = cv.imread(path)
    # convert to grayscale picture
    grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # transform to binary
    (thresh, binaryImage) = cv.threshold(grayImg, 127, 255, cv.THRESH_BINARY)
    # save to disc
    cv.imwrite("images/binary.png", binaryImage)
