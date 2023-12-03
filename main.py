# import os
#
# import cv2 as cv
# import numpy as np
#
# # Change the working directory to the folder this script is in.
# os.chdir(os.path.dirname(os.path.abspath(__file__)))
#
# attack_image = cv.imread("./src/assets/builder_attack_button.png")
# find_now_image = cv.imread("./src/assets/builder_find_now.png")
#
# result = cv.matchTemplate(
#     attack_image,
#     find_now_image,
#     cv.TM_CCOEFF_NORMED
# )
#
# min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
#
# print(f"Best match top left position: {max_loc}")
# print(f"Best match confidence: {max_val}")


import cv2 as cv
import os
from time import time

import pyautogui

from src.vision.vision import Vision
from src.window_capture.window_capture import WindowCapture

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# initialize the WindowCapture class
wincap = WindowCapture('Clash of Clans')
# initialize the Vision class
attack_button = Vision('resource/assets/builder_attack_button.png')


loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    # display the processed image
    points = attack_button.find(screenshot, 0.7, 'rectangles')
    #points = vision_gunsnbottle.find(screenshot, 0.7, 'points')

    # coord_x = wincap.offset_x + points[0][0]
    # coord_y = wincap.offset_y + points[0][1]

    # pyautogui.moveTo(coord_x, coord_y)



    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')