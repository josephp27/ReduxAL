import threading
import time

from mouse_events.mover import move_mouse


class gun_settings:

    def __init__(self, enabled=False):
        self.enabled = enabled

    def pull_down_r301(self, parent):
        count = 0
        sleep_time = 0.0005

        # while the left mouse button is held
        while parent.enabled:
            print(self.enabled, 'r301', end='\r', flush=True)

            # do some weird delaying
            count += 1
            if count % 10 == 0:
                sleep_time += 0.01
            if 30 < count < 40:
                # spawn a thread call the function move mouse going left by one pixel
                threading.Thread(target=move_mouse, args=(-1, 0,)).start()

            # spawn a threads call the function move mouse to move one pixel down
            threading.Thread(target=move_mouse, args=(0, 1,)).start()

            # sleep to delay
            time.sleep(sleep_time)

    def pull_down_prowler(self, parent):
        sleep_time = 0.002

        # while left mouse button is pressed
        while parent.enabled:
            print(self.enabled, 'prowler', end='\r', flush=True)

            # spawn a threads call the function move mouse to move one pixel down
            threading.Thread(target=move_mouse, args=(0, 1,)).start()

            # sleep by some predetermined time
            time.sleep(sleep_time)

    def pull_down_devotion(self, parent):
        # insert custom code below
        print(self.enabled, 'devotion', end='\r', flush=True)

    def pull_down_havoc(self, parent):
        # insert custom code below
        print(self.enabled, 'havoc', end='\r', flush=True)

    def pull_down_tripletake(self, parent):
        # insert custom code below
        print(self.enabled, 'tripletake', end='\r', flush=True)

    def pull_down_flatline(self, parent):
        # insert custom code below
        print(self.enabled, 'flatline', end='\r', flush=True)

    def pull_down_hemlok(self, parent):
        # insert custom code below
        print(self.enabled, 'hemlok', end='\r', flush=True)

    def pull_down_longbow(self, parent):
        # insert custom code below
        print(self.enabled, 'longbow', end='\r', flush=True)

    def pull_down_spitfire(self, parent):
        # insert custom code below
        print(self.enabled, 'spitfire', end='\r', flush=True)

    def pull_down_wingman(self, parent):
        # insert custom code below
        print(self.enabled, 'wingman', end='\r', flush=True)

    def pull_down_kraber(self, parent):
        # insert custom code below
        print(self.enabled, 'kraber', end='\r', flush=True)

    def pull_down_mastiff(self, parent):
        # insert custom code below
        print(self.enabled, 'mastiff', end='\r', flush=True)

    def pull_down_alternator(self, parent):
        # insert custom code below
        print(self.enabled, 'alternator', end='\r', flush=True)

    def pull_down_g7scout(self, parent):
        # insert custom code below
        print(self.enabled, 'g7scout', end='\r', flush=True)

    def pull_down_p2020(self, parent):
        # insert custom code below
        print(self.enabled, 'p2020', end='\r', flush=True)

    def pull_down_r99(self, parent):
        # insert custom code below
        print(self.enabled, 'r99', end='\r', flush=True)

    def pull_down_re45(self, parent):
        # insert custom code below
        print(self.enabled, 're45', end='\r', flush=True)

    def pull_down_eva8(self, parent):
        # insert custom code below
        print(self.enabled, 'eva8', end='\r', flush=True)

    def pull_down_mozambique(self, parent):
        # insert custom code below
        print(self.enabled, 'mozambique', end='\r', flush=True)

    def pull_down_peacekeeper(self, parent):
        # insert custom code below
        print(self.enabled, 'peacekeeper', end='\r', flush=True)

