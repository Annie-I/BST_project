import cv2 as cv
import numpy as np
import helpers.image_processing as image
import helpers.trackbars as trackbars

bw_picture = "images/binary.png"
blurred_picture = "images/blurred.png"
result_window = "Result"

def contours(path):
    # create trackbars
    trackbars.canny_min_max()
    trackbars.contour_area_min_max()

    while True:
        # get trackbar min and max threshold variables
        min_threshold = cv.getTrackbarPos("Min Threshold", "Trackbar")
        max_threshold = cv.getTrackbarPos("Max Threshold", "Trackbar")
        min_area = cv.getTrackbarPos("Min Area", "Trackbar")
        max_area = cv.getTrackbarPos("Max Area", "Trackbar")
        # read the original image
        original_img = cv.imread(path)
        #convert to binary
        image.convertToBinary(path)
        # blure the image, to avoid edge brakes
        image.blur(bw_picture)
        # read the transformed image
        img = cv.imread(blurred_picture)
        imgBw = cv.imread(bw_picture)
        # create empty image
        imgBlank = np.zeros_like(img)
        # get the edges
        edged = cv.Canny(img, min_threshold, max_threshold, 3)
        # get the contours
        # RETR_EXTERNAL - get the extreme outer contours
        contours, hierarchy = cv.findContours(edged, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE) # last one is to get all of the contour points

        for contour in contours:
            area = cv.contourArea(contour)

            if (area > min_area) and (area < max_area):
                # draw the contours
                # (where to draw, what to draw, how many (negative value for all of them), (color), thickness (1 by default))
                cv.drawContours(imgBw, contour, -1, (0, 0, 255), 2)

                # get the center
                M = cv.moments(contour)
                if M["m00"] != 0:
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])
                else:
                    cX, cY = 0, 0
                cv.circle(imgBw, (cX, cY), 2, (0, 255, 0), -1)

        # display to user
        cv.imshow(result_window, imgBw) # name of the output window + image to display
        # print objects found
        # delay closing image output window to see the picture (ms, but 0 is infinite)
        if cv.waitKey(500) & 0xFF == ord('q'):
            image.save("contours", imgBw)
            print("Attēls saglabāts")

            break

