import numpy as np
from PIL import ImageGrab, ImageEnhance, Image
import cv2
import time
import keyboard
import time
import mouse as m
import random


count = 0
def grab_screen():
    global count
    global im
    screen = ImageGrab.grab(bbox=(1550,1030,1670,1055))
    screen.save("data\\primary.jpeg",'jpeg')

    screen = ImageGrab.grab(bbox=(1700,1030,1820,1055))
    screen.save("data\\secondary.jpeg",'jpeg')
    count += 1


def mousey():
    grab_screen()
    print("button clicked")

m.on_right_click(mousey)

# Block forever, like `while True`.
keyboard.wait()