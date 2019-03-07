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
from mover import move_mouse
from pynput import mouse
import os
import signal
import threading

training_data = []
should_pull_down = True

def fillTraining(path): 
        global training_data 
        
        if 'jpeg' in path:
                im = Image.open(path)
                tokens = path.split('/')
                training_data.append((im, tokens[3:5]))
                return

        for type_ in os.listdir(path):
                fillTraining(path + '/' + type_)


fillTraining(os.getcwd() + '/data')

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
    best_data = []
    for im, data in training_data:
        error = min(mse(primary, np.asarray(im)), mse(secondary, np.asarray(im)))
        if error < min_:
            min_ = error
            best_data = data

    print(min_, best_data)


enabled = False
def pull_down(press):
    while 1:
        global enabled
        enabled = press
        print(enabled, end='\r', flush=True)
        while enabled == True:
            print(enabled, end='\r', flush=True)
            threading.Thread(target=move_mouse, args=(1,)).start()
            time.sleep(0.005)


def mousey(call):
    if isinstance(call, m.WheelEvent):
        time.sleep(0.05)
        grab_screen()
    
def keyboardy(call):
    time.sleep(0.05)
    grab_screen()

def quitter(call):
    print("quitting")
    os.kill(os.getpid(),signal.SIGTERM)

m.hook(mousey)
keyboard.on_release_key('e', keyboardy)
keyboard.on_release_key('l', quitter)

def on_click(x, y, button, pressed):
    global enabled
    if button == mouse.Button.left and pressed == True:
        enabled = True
    else:
        enabled = False

t = threading.Thread(target=pull_down, args=(False,))
t.start()
# Collect events until released
with mouse.Listener(on_click=on_click) as listener:
    listener.join()

