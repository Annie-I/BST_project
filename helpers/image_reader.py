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

# TO-DO: not done!
def getCircles(path):
    # read the image
    img = cv.imread(path)
    # convert to grayscale picture
    grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # transform to binary
    (thresh, binaryImage) = cv.threshold(grayImg, 127, 255, cv.THRESH_BINARY)
    #create copy of binary image
    result = binaryImage.copy()

    # save to disc
    cv.imwrite("images/binaryWithCircles.png", result)

    # detect circles in the image
    circles = cv.HoughCircles(result, cv.HOUGH_GRADIENT, 1.2, 100)

    # ensure at least some circles were found
    if circles is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")
        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:
            # draw the circle in the output image
            cv.circle(result, (x, y), r, (0, 255, 0), 4)

        cv.imshow("result", result)
        cv.waitKey(0)

