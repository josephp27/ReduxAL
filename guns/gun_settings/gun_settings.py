import threading
import time

from mouse_events.mover import move_mouse


class gun_settings:

    def __init__(self, enabled=False):
        self.enabled = enabled

    def pull_down_r301(self, parent):
        count = 0
        sleep_time = 0.0005

        while parent.enabled:
            print(self.enabled, 'r301', end='\r', flush=True)
            count += 1
            if count % 10 == 0:
                sleep_time += 0.002
            if 48 < count < 53:
                threading.Thread(target=move_mouse, args=(-3, 0,)).start()

            threading.Thread(target=move_mouse, args=(0, 1,)).start()
            time.sleep(sleep_time)
