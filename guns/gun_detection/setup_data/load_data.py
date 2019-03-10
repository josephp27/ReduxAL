import os

from PIL import Image

training_data = []


def fill_training_data(path):
    global training_data

    if 'jpeg' in path:
        im = Image.open(path)
        tokens = path.split('/')
        training_data.append((im, tokens[3:5]))
        return

    for type_ in os.listdir(path):
        fill_training_data(path + '/' + type_)


def load_data(path):
    fill_training_data(path)
    return training_data
