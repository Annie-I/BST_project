#from email.mime import image
import cv2 as cv
import math
import numpy as np
import helpers.image_processing as image
import helpers.draw as draw

def angles(path):
    # read the image
    selected_points = []
    img = cv.imread(path)

    def mark_points(event, x, y, flags, param):
        if event == cv.EVENT_LBUTTONDOWN:
            cv.circle(img, (x, y), 3, (110, 255, 255), cv.FILLED)
            #if (len(selected_points) != 0):
                #cv.arrowedLine(img, tuple(selected_points[0]), (x, y), (0, 255, 0), 2)
            selected_points.append([x, y])
            #print(selected_points)

    def vector(pt1, pt2):
        return (pt2[1] - pt1[1]) / (pt2[0] - pt1[0])

    def find_angle(points):
        a = points[-2]
        b = points[-3]
        c = points[-1]

        cv.line(img, (b[0], b[1]), (a[0], a[1]), (0, 255, 0), 2)
        cv.line(img, (b[0], b[1]), (c[0], c[1]), (0, 255, 0), 2)

        m1 = vector(b, a)
        m2 = vector(b, c)

        radians = math.atan((m2 - m1) / (1+m1*m2))
        degrees = round(math.degrees(radians), 2)
        # for angles >90° to be correct
        if (degrees < 0):
            degrees = degrees + 180

        cv.putText(img, str(degrees), (b[0]+5, b[1]+35), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv.LINE_8)
        cv.imshow ("Image", img)

    while True:
        if len(selected_points) % 3 == 0 and len(selected_points) != 0:
            find_angle(selected_points)
        if len(selected_points) > 2:
            selected_points = []

        cv.imshow("Image", img)
        cv.setMouseCallback("Image", mark_points)
        if cv.waitKey(1) & 0xFF == ord('r'):
            selected_points = []
            img = cv.imread(path)
            cv.imshow("Image", img)
            cv.setMouseCallback("Image", mark_points)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break