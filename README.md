# ApexLegendsGunClassifier

import os
from PIL import ImageGrab, ImageEnhance, Image


training_data = []

def fillTraining(path):
    global training_data
    tokens = path.split('/')

    if 'jpeg' in path:
        im = Image.open(path)
        training_data.append((im, tokens[1], tokens[2]))
        return

    for type_ in os.listdir(path):
        if '.DS_Store' in type_:
            continue
        fillTraining(path + '/' + type_)



fillTraining(os.getcwd() + '/data')

print(training_data)
