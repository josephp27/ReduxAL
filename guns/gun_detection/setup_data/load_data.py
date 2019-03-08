import os 
from PIL import ImageGrab, ImageEnhance, Image

training_data = []
def fillTraining(path): 
        global training_data 
        
        if 'jpeg' in path:
                im = Image.open(path)
                tokens = path.split('/')
                training_data.append((im, tokens[3:5]))
                return

        for type_ in os.listdir(path):
                fillTraining(path + '/' + type_)

def load_data(path):
    fillTraining(path)
    return training_data