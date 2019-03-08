from .mover import move_mouse
import threading
import time

class mouse_pull_down:
    def __init__(self, enabled=False):
        self.enabled = enabled

    def pull_down(self, press):
        while 1:
            self.enabled = press
            print(self.enabled, end='\r', flush=True)
                
            while self.enabled == True:
                print(self.enabled, end='\r', flush=True)
                threading.Thread(target=move_mouse, args=(1,)).start()
                time.sleep(0.005)