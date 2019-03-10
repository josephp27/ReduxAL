def pull_down_listener(func):
    def loop(self, press):
        while 1:
            func(self)

    return loop
