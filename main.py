#import imp
from sre_constants import SUCCESS
import cv2 as cv
import math
#import helpers.image_processing as image
import helpers.detect as detect
import helpers.draw as draw
import helpers.calculations as get

camera_id = 0
colored_picture = "images/colors.jpg"
gray_picture = "images/grayscale.png"
bw_picture = "images/binary.png"
video = "images/video.mp4"
detected_edges = "images/edges.png"
blurred_picture = "images/blurred.png"
dots = "images/contours.png"

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
# image.convertToBinary(colored_picture)
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
# print("Sāk meklēt kontūras")
# detect.contours(colored_picture)
# print("Kontūru meklēšana pabeigta")

# <<<--- Read and display camera stream --->>>
# print("kameras stream sākums")
# read.stream()
# print("kameras stream beigas")

# <<<--- Read and display video --->>>
# print("video sākums")
# read.video(video)
# print("video beigas")

#Result:
# ------
# <<<--- Read an image, detect circles and connect them with lines --->>>
print ("Sāk meklēt apļus")
detect.contours(colored_picture)
print ("Apļus savienošana pabeigta")
cv.destroyAllWindows()

# <<<--- Read an image, mark points and calculate the angle between them --->>>
print ("Var sākt meklēt leņķus. Pirmais punkts - virsotne, otrais - pa kreisi no pirmā vai augstāk par to, ja uz 1 līnijas")
get.angles(dots)
print ("leņķu meklēšāna beigusies")

# <<<--- Close opened windows --->>>
cv.destroyAllWindows()
print("Programmas darbības beigas")