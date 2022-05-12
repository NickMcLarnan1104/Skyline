# PROGRAMMER: Nick McLarnan
# PROGRAM NAME: Assignment 10 - City Skyline
# DATE WRITTEN: 04/13/2022
# PURPOSE: Use functions to create a city skyline using turtle module


import turtle
import random
from myCustomFunctions import *

# Main function
def drawCity_Skyline():
    # Call function to set-up screen
    setup_Screen()

    # Call function to draw stars
    # STARS ARE PLACED RANDOMLY
    draw_Stars()

    # Call function to draw buildings
    draw_Building()

    # Call function to draw windows
    draw_Window()

drawCity_Skyline()

# Functions are saved at bottom of myCustomFunctions file

# END PROGRAM
