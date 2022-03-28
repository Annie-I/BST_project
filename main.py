from sre_constants import SUCCESS
import cv2 as cv
import numpy as np
import helpers.video_reader as video_reader
import helpers.image_reader as image_reader
import helpers.camera_reader as camera_reader

camera_id = 0

# <<<--- Read and display picture as it is --->>>
# print("bilde:")
# image_reader.displayAsIs("images/colors.png")
# print("bilde beidzās")

# <<<--- Read and display picture as grayscale --->>>
# print("krāsaina bilde uz melnbaltu:")
# image_reader.displayGrayscale("images/colors.png")
# print("melnbalta bilde beidzās")

# <<<--- Read and display picture as binary (black and white) --->>>
# print("melnbalta bilde uz bināru:")
# image_reader.displayBinary("images/colors.png")
# print("bināra bilde beidzās")

# <<<--- Transform picture to binary and save it without displaying it --->>>
# print("Sāk pārveidošānu uz bināru attēlu:")
# image_reader.saveBinary("images/colors.png")
# print("Bilde veiksmīgi apstrādāta un saglabāta")

# <<<--- Read and display camera stream --->>>
# print("kameras stream sākums")
# camera_reader.stream()
# print("kameras stream beigas")

# <<<--- Read and display video --->>>
# print("video sākums")
# video_reader.play("images/video.mp4")
# print("video beigas")

cv.destroyAllWindows()