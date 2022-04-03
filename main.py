from sre_constants import SUCCESS
import cv2 as cv
import numpy as np
import helpers.media_reader as read
import helpers.image_processing as image
import helpers.draw as draw
import helpers.detect as detect

camera_id = 0
colored_picture = "images/colors.jpg"
gray_picture = "images/grayscale.png"
bw_picture = "images/binary.png"
video = "images/video.mp4"
detected_edges = "images/edges.png"
blurred_picture = "images/blurred.png"

# <<<--- Read and display picture as it is --->>>
# print("bilde:")
# image.displayAsIs(colored_picture)
# print("bilde beidzās")

# <<<--- Read an image. transform it to grayscale, save it to disc and display it to user --->>>
# print("Sāk pārveidošānu uz pelēku attēlu")
# image.convertToGrayscale(colored_picture)
# print("Pārveidošana uz pelēku bildi veiksmīgi izdevusies")

# <<<--- Read an image, transform it to binary (black and white), save it to disc and display it to user  --->>>
# print("Sāk pārveidošānu uz bināru attēlu")
# image.toBinary(colored_picture)
# print("Pārveidošana veiksmīgi izdevusies")

# <<<--- Read image, find edges in it, display it to user and save to disc --->>>
# print("Sāk malu meklēšanu:")
# image.getEdges(blurred_picture)
# print("Malu meklēšana pabeigta")

# <<<--- Read an image, draw a line in it and display it to user --->>>
# print("Sāk zīmēt līniju")
# draw.line(bw_picture)
# print("Līnijas zīmēšana pabeigta")

# <<<--- Read an image, draw a circle in it and display it to user --->>>
# print("Sāk zīmēt apli")
# draw.circle(bw_picture)
# print("Apļa zīmēšana pabeigta")

# <<<--- Read an image, detect contours in it and display the result to user --->>>
print("Sāk meklēt kontūras")
detect.contours(colored_picture)
print("Kontūru meklēšana pabeigta")

# <<<--- Read and display camera stream --->>>
# print("kameras stream sākums")
# read.stream()
# print("kameras stream beigas")

# <<<--- Read and display video --->>>
# print("video sākums")
# read.video(video)
# print("video beigas")

# <<<--- Close opened windows --->>>

cv.destroyAllWindows()
print("Programmas darbības beigas")