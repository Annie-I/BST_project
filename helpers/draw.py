from copy import copy
from sys import call_tracing
from webbrowser import get
import cv2 as cv
import helpers.detect as detected
import helpers.image_processing as image
import helpers.calculations as calculate

colored_picture = "images/colors.jpg"
contoured_picture = "images/contours.png"
lines = "images/lines.png"

#funtion to draw a line
def line(path, start_width, start_height, end_width, end_height):
    # read the image
    img = cv.imread(path)
    # draw the circle
    # (where to draw, (starting point), (ending point), (color), thickness)
    cv.line(img, (start_width, start_height), (end_width, end_height), (0, 255, 0), 2)
    # image.save("lines", img)


#funtion to draw a circle
def circle(path):
    # read the image
    img = cv.imread(path)
    # draw the circle
    # (where to draw, (center point), (radius), (color), thickness)
    cv.circle(img, (300, 250), 12, (0, 0, 255), cv.FILLED)
    # display to user
    cv.imshow("Image with a drawing", img) # name of the output window + image to display
    cv.waitKey(0) # delay closing image output window to see the picture (ms, but 0 is infinite)


def connect_dots():
    copy_for_lines = cv.imread(contoured_picture)
    image.save("lines", copy_for_lines)

    detected.contours(colored_picture)

    # Metacarpal - Carpal
    MC1 = [detected.points[0], detected.points[1]]
    MC2 = [detected.points[2], detected.points[3]]
    MC3 = [detected.points[4], detected.points[5]]
    MC4 = [detected.points[8], detected.points[9]]
    MC5 = [detected.points[6], detected.points[7]]
    # Phalanges
    # Proximal - Metacarpal
    PM1 = [detected.points[10], detected.points[11]]
    PM2 = [detected.points[22], detected.points[23]]
    PM3 = [detected.points[20], detected.points[21]]
    PM4 = [detected.points[16], detected.points[17]]
    PM5 = [detected.points[14], detected.points[15]]

    # Middle - Proximal
    MP2 = [detected.points[30], detected.points[31]]
    MP3 = [detected.points[32], detected.points[33]]
    MP4 = [detected.points[28], detected.points[29]]
    MP5 = [detected.points[24], detected.points[25]]

    # Distal - Middle
    DM2 = [detected.points[38], detected.points[39]]
    DM3 = [detected.points[40], detected.points[41]]
    DM4 = [detected.points[36], detected.points[37]]
    DM5 = [detected.points[26], detected.points[27]]

    #Distal - Proximal (Thumb)
    DP1 = [detected.points[12], detected.points[13]]

    # Tips
    D1 = [detected.points[18], detected.points[19]]
    D2 = [detected.points[42], detected.points[43]]
    D3 = [detected.points[46], detected.points[47]]
    D4 = [detected.points[44], detected.points[45]]
    D5 = [detected.points[34], detected.points[35]]

    # Thumb
    line(lines, MC1[0], MC1[1], PM1[0], PM1[1])
    line(lines, PM1[0], PM1[1], DP1[0], DP1[1])
    line(lines, DP1[0], DP1[1], D1[0], D1[1])

    # Index finger
    line(lines, MC2[0], MC2[1], PM2[0], PM2[1])
    line(lines, PM2[0], PM2[1], MP2[0], MP2[1])
    line(lines, MP2[0], MP2[1], DM2[0], DM2[1])
    line(lines, DM2[0], DM2[1], D2[0], D2[1])

    # Middle finger
    line(lines, MC3[0], MC3[1], PM3[0], PM3[1])
    line(lines, PM3[0], PM3[1], MP3[0], MP3[1])
    line(lines, MP3[0], MP3[1], DM3[0], DM3[1])
    line(lines, DM3[0], DM3[1], D3[0], D3[1])

    # Ring finger
    line(lines, MC4[0], MC4[1], PM4[0], PM4[1])
    line(lines, PM4[0], PM4[1], MP4[0], MP4[1])
    line(lines, MP4[0], MP4[1], DM4[0], DM4[1])
    line(lines, DM4[0], DM4[1], D4[0], D4[1])

    # Pinky
    line(lines, MC5[0], MC5[1], PM5[0], PM5[1])
    line(lines, PM5[0], PM5[1], MP5[0], MP5[1])
    line(lines, MP5[0], MP5[1], DM5[0], DM5[1])
    line(lines, DM5[0], DM5[1], D5[0], D5[1])

    # display to user
    #image.displayAsIs(lines)