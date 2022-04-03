import cv2 as cv
import helpers.image_processing as image
import numpy as np

bw_picture = "images/binary.png"
blurred_picture = "images/blurred.png"

def contours(path):
    # read the original image
    original_img = cv.imread(path)
    #convert to binary
    image.convertToBinary(path)
    # blure the image, to avoid edge brakes
    image.blur(bw_picture)
    # read the transformed image
    img = cv.imread(blurred_picture)
    img_bw = cv.imread(bw_picture)
    # get the edges
    edged = cv.Canny(img, 700, 850, 3)
    # get the contours
    contours, hierarchy = cv.findContours(edged, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE) # last one is to get all of the contour points
    # draw the contours
    # (where to draw, what to draw, how many (negative value for all of them), (color), thickness (1 by default))
    cv.drawContours(original_img, contours, -1, (0, 0, 255))
    # display to user
    cv.imshow("Contours", original_img) # name of the output window + image to display
    cv.waitKey(0) # delay closing image output window to see the picture (ms, but 0 is infinite)