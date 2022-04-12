import cv2 as cv
import numpy as np

def save(file_name, data):
    cv.imwrite("images/"+ file_name +".png", data)

# function to read picture and show to user
def displayAsIs(path):
    # read the image
    img = cv.imread(path)
    # print image size
    print(img.shape)
    # display to user
    cv.imshow("Original image", img) # name of the output window + image to display
    cv.waitKey(0) # delay closing image output window to see the picture (ms, but 0 is infinite)

# function to read picture, convert it to grayscale and show to user
def convertToGrayscale(path):
    # read the image
    img = cv.imread(path)
    # convert to grayscale picture
    grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # save to disc
    save("grayscale", grayImg)
    # display to user
    #cv.imshow("Gray image", grayImg) # name of the output window + image to display
    #cv.waitKey(0) # delay closing image output window to see the picture (ms, but 0 is infinite)

# function to read picture, convert it to binary and save it to disc
def convertToBinary(path):
    # read the image
    img = cv.imread(path)
    # convert to grayscale picture
    grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # transform to binary
    (thresh, binaryImage) = cv.threshold(grayImg, 127, 255, cv.THRESH_BINARY)
    # save to disc
    save("binary", binaryImage)
    # display to user
    #cv.imshow("Binary image", binaryImage) # name of the output window + image to display
    #cv.waitKey(0) # delay closing image output window to see the picture (ms, but 0 is infinite)

def blur(path):
    # read the image
    img = cv.imread(path)
    # blur the image
    blurred_img = cv.GaussianBlur(img, (3, 3), 0)
    # save to disc
    save("blurred", blurred_img)
    # display to user
    #cv.imshow("Blurred image", blurred_img) # name of the output window + image to display
    #cv.waitKey(0) # delay closing image output window to see the picture (ms, but 0 is infinite)

# function to detect edges that displays and saves the result to disc
def getEdges(path):
    # read the image
    img = cv.imread(path)
    # get the edges
    # (image, lower threshold, highest threshold, number of edges(odd num 3-7 where 7 = most details))
    imgCanny = cv.Canny(img, 700, 850, 3)
    # display to user
    cv.imshow("Edges", imgCanny) # name of the output window + image to display
    cv.waitKey(0) # delay closing image output window to see the picture (ms, but 0 is infinite)
    # save to disc
    save("edges", imgCanny)

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
