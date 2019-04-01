from guns.gun_settings.gun_settings import gun_settings
from mouse_events.decorators import pull_down_listener

# instantiate our class with enabled set to False
guns = gun_settings(False)


class mouse_pull_down:

    def __init__(self, enabled=False, equipped_gun=None):
        self.enabled = enabled
        self.equipped_gun = equipped_gun

    @pull_down_listener
    def pull_down(self):

        print(self.enabled, end='\r', flush=True)
        # energy
        if self.equipped_gun == 'devotion':
            guns.pull_down_devotion(self)

        elif self.equipped_gun == 'havoc':
            guns.pull_down_havoc(self)

        elif self.equipped_gun == 'tripletake':
            guns.pull_down_tripletake(self)

        # heavy
        elif self.equipped_gun == 'prowler':
            guns.pull_down_prowler(self)

        elif self.equipped_gun == 'flatline':
            guns.pull_down_flatline(self)

        elif self.equipped_gun == 'hemlok':
            guns.pull_down_hemlok(self)

        elif self.equipped_gun == 'longbow':
            guns.pull_down_longbow(self)

        elif self.equipped_gun == 'spitfire':
            guns.pull_down_spitfire(self)

        elif self.equipped_gun == 'wingman':
            guns.pull_down_wingman(self)

        # legendary
        elif self.equipped_gun == 'kraber':
            guns.pull_down_kraber(self)

        elif self.equipped_gun == 'mastiff':
            guns.pull_down_mastiff(self)

        # light
        elif self.equipped_gun == 'alternator':
            guns.pull_down_alternator(self)

        elif self.equipped_gun == 'g7scout':
            guns.pull_down_g7scout(self)

        elif self.equipped_gun == 'p2020':
            guns.pull_down_p2020(self)

        elif self.equipped_gun == 'r99':
            guns.pull_down_r99(self)

        elif self.equipped_gun == 'r301':
            guns.pull_down_r301(self)

        elif self.equipped_gun == 're45':
            guns.pull_down_re45(self)

        # shotgun
        elif self.equipped_gun == 'eva8':
            guns.pull_down_eva8(self)

        elif self.equipped_gun == 'mozambique':
            guns.pull_down_mozambique(self)

        elif self.equipped_gun == 'peacekeeper':
            guns.pull_down_peacekeeper(self)
