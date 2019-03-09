import time
import keyboard
import mouse as m
import random
import os
from pynput import mouse
import os
import signal
import threading
from guns.gun_detection.detect_gun import detect_gun
from guns.gun_detection.setup_data.load_data import load_data
from mouse_events.mouse_pull_down.pull_down import mouse_pull_down

training_data = load_data(os.getcwd() + '/data')
equipped_gun = detect_gun(training_data)
puller = mouse_pull_down()

def mouse_handler(call):
    if isinstance(call, m.WheelEvent):
        time.sleep(0.05)
        equipped_gun.detect()
        puller.equipped_gun = 'gun'
    
def keyboard_handler(call):
    time.sleep(0.05)
    equipped_gun.detect()
    puller.equipped_gun = 'gun'

def quit_handler(call):
    print("quitting")
    os.kill(os.getpid(),signal.SIGTERM)

def on_click_handler(x, y, button, pressed):
    if button == mouse.Button.left and pressed == True:
        puller.enabled = True
    else:
        puller.enabled = False

if __name__ == "__main__":
    
    threading.Thread(target=puller.pull_down, args=(False,)).start()

    # enable listening to keyboard and mouse events
    m.hook(mouse_handler)
    keyboard.on_release_key('e', keyboard_handler)
    keyboard.on_release_key('l', quit_handler)
    with mouse.Listener(on_click=on_click_handler) as listener:
        listener.join()