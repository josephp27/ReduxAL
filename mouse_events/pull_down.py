from guns.gun_settings.gun_settings import gun_settings

a = gun_settings(False)


class mouse_pull_down:
    def __init__(self, enabled=False, equipped_gun=None):
        self.enabled = enabled
        self.equipped_gun = equipped_gun

    # noinspection PyMethodParameters
    def pull_down_listener(func):
        def loop(self, press):
            while 1:
                print(self.enabled, end='\r', flush=True)
                func(self)

        return loop

    @pull_down_listener
    def pull_down(self):

        if self.equipped_gun == 'r301':
            a.pull_down_r301(self)