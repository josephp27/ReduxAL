from guns.gun_settings.gun_settings import gun_settings
from mouse_events.decorators import pull_down_listener

a = gun_settings(False)


class mouse_pull_down:

    def __init__(self, enabled=False, equipped_gun=None):
        self.enabled = enabled
        self.equipped_gun = equipped_gun

    @pull_down_listener
    def pull_down(self):

        print(self.enabled, end='\r', flush=True)
        if self.equipped_gun == 'r301':
            a.pull_down_r301(self)
