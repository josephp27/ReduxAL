import numpy as np

from .win32_screen import grab_screen as grabby


class detect_gun:

    def __init__(self, training_data=None):
        self.training_data = training_data

    def mse(self, image_a, image_b):
        # the 'Mean Squared Error' between the two images is the
        # sum of the squared difference between the two images;
        # NOTE: the two images must have the same dimension
        err = np.sum((image_a.astype("float") - image_b.astype("float")) ** 2)
        err /= float(image_a.shape[0] * image_a.shape[1])

        # return the MSE, the lower the error, the more "similar"
        # the two images are
        return err

    def detect(self):
        global im
        primary = grabby(region=(1550, 1030, 1669, 1054))
        secondary = grabby(region=(1700, 1030, 1819, 1054))

        min_ = 500
        best_data = []
        for im, data in self.training_data:
            error = min(self.mse(primary, np.asarray(im)), self.mse(secondary, np.asarray(im)))
            if error < min_:
                min_ = error
                best_data = data

        print(min_, best_data)
        return best_data[0] if len(best_data) > 0 else None
