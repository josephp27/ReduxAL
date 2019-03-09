from .mover import move_mouse
import threading
import time

class mouse_pull_down:
    def __init__(self, enabled=False, equipped_gun=None):
        self.enabled = enabled
        self.equipped_gun = equipped_gun

    def pull_down(self, press):
        while 1:
            self.enabled = press
            print(self.enabled, end='\r', flush=True)
            
            count = 0
            sleep_time = 0.0005
            while self.enabled == True:
                count += 1
                if count % 10 == 0:
                    sleep_time += 0.002
                if count > 48 and count < 53:
                    threading.Thread(target=move_mouse, args=(-3,0,)).start()
                print(self.enabled, self.equipped_gun, end='\r', flush=True)
                threading.Thread(target=move_mouse, args=(0,1,)).start()
                time.sleep(sleep_time)