import numpy as np
from PIL import ImageGrab, ImageEnhance, Image
from win32_screen import grab_screen as grabby
import cv2
import time
import keyboard
import time
import mouse as m
import random
import os
import numpy as np
from PIL import Image
import cv2

training_data = []
for ammo_type in os.listdir(os.getcwd() + '/data/'):
    for gun in os.listdir(os.getcwd() + '/data/' + str(ammo_type)):
        for gun_pos in os.listdir(os.getcwd() + '/data/' + ammo_type + '/' + gun):
            for filename in os.listdir(os.getcwd() + '/data/' + ammo_type + '/' + gun + '/' + gun_pos):
                im = Image.open(os.getcwd() + '/data/' + ammo_type + '/' + gun + '/' + gun_pos + '/' + filename)
                training_data.append((im, gun, gun_pos))


def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err

def grab_screen():
    global im
    primary = grabby(region=(1550,1030,1669,1054))
    secondary = grabby(region=(1700,1030,1819,1054))

    min_ = 500
    best_guess_gun = ''
    best_guess_gun_pos = ''
    for im, gun, gun_pos in training_data:
        error = min(mse(primary, np.asarray(im)), mse(secondary, np.asarray(im)))
        if error < min_:
            min_ = error
            best_guess_gun = gun
            best_guess_gun_pos = gun_pos

    print(min_, best_guess_gun, best_guess_gun_pos)


def mousey(call):
    if isinstance(call, m.WheelEvent):
        time.sleep(0.05)
        grab_screen()

def keyboardy(call):
    time.sleep(0.05)
    grab_screen()

m.hook(mousey)
keyboard.on_release_key('e', keyboardy)
# Block forever, like `while True`.
keyboard.wait()