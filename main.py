from sre_constants import SUCCESS
import cv2 as cv
import numpy as np
import helpers.media_reader as read
import helpers.image_processing as image
import helpers.draw as draw

camera_id = 0
colored_picture = "images/colors.jpg"
bw_picture = "/images/binary.png"
video = "/images/video.mp4"

# <<<--- Read and display picture as it is --->>>
# print("bilde:")
# image.displayAsIs(colored_picture)
# print("bilde beidzās")

# <<<--- Read and display picture as grayscale --->>>
# print("krāsaina bilde uz melnbaltu:")
# image.displayGrayscale(colored_picture)
# print("melnbalta bilde beidzās")

# <<<--- Read and display picture as binary (black and white) --->>>
# print("melnbalta bilde uz bināru:")
# image.displayBinary(colored_picture)
# print("bināra bilde beidzās")

# <<<--- Transform picture to binary and save it without displaying it --->>>
# print("Sāk pārveidošānu uz bināru attēlu:")
# image.saveBinary(colored_picture)
# print("Bilde veiksmīgi apstrādāta un saglabāta")

# <<<--- Read image, find edges in it, display it to user and save to disc --->>>
# print("Sāk malu meklēšanu:")
# image.getEdges(bw_picture)
# print("Malu meklēšana pabeigta")

# <<<--- Read image, draw a line in it and display it to user --->>>
# print("Sāk zīmēt")
# draw.line(bw_picture)
# print("Zīmēšana pabeigta")

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