import cv2 as cv

def nothing(x):
    pass

def canny_min_max():
    # create empty window where to place trackbars
    cv.namedWindow("Trackbar")
    # create trackbar for min threshold value
    # (trackbar name, window name where to display it, starting value, max value, f on change)
    cv.createTrackbar("Min Threshold", "Trackbar", 0, 1000, nothing)
    # create trackbar for max threshold value
    cv.createTrackbar("Max Threshold", "Trackbar", 0, 1000, nothing)

# TO-DO - could create trackbar for blur as well