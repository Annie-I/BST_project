# import imp
#from turtle import circle
import cv2 as cv
import numpy as np

# function to read picture and show to user
def displayAsIs(path):
    # read the image
    img = cv.imread(path)
    # print image size
    print(img.shape)
    # display to user
    cv.imshow("Original image", img) # name of the output window + image to display
    cv.waitKey(0) # delay closing image output window to see the picture (ms, but 0 is infinite)

    cv.destroyAllWindows()

# function to read picture, convert it to grayscale and show to user
def displayGrayscale(path):
    # read the image
    img = cv.imread(path)
    # convert to grayscale picture
    grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # display to user
    cv.imshow("Gray image", grayImg) # name of the output window + image to display
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
    cv.imshow("Binary image", binaryImage) # name of the output window + image to display
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

# function to detect edges that displays and saves the result to disc
def getEdges(path):
    # read the image
    img = cv.imread(path)
    # get the edges
    imgCanny = cv.Canny(img, 100, 100) # (image, threshold, threshold)
    # display to user
    cv.imshow("Edges", imgCanny) # name of the output window + image to display
    cv.waitKey(0) # delay closing image output window to see the picture (ms, but 0 is infinite)
    # save to disc
    cv.imwrite("images/edges.png", imgCanny)

# function to thicken the edges
def thickenEdges(path):
    # read the image
    img = cv.imread(path)
    # set kernel: create 5x5 matrix filled with ones and object type - unsigned 8 bit integer (0-255)
    kernel = np.ones((5, 5), np.uint8)
    # widen the edges
    imgDialation = cv.dilate(img, kernel, iterations=1) # img, kernel and iterations
    # display to user
    cv.imshow("Thicker edges", imgDialation) # name of the output window + image to display
    cv.waitKey(0) # delay closing image output window to see the picture (ms, but 0 is infinite)
