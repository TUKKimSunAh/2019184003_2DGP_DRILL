from pico2d import *

class Grass1:
    image = None

    def __init__(self, x= 400,y= 60):
        if Grass1.image == None:
            Grass1.image = load_image('grass.png')

        self.x, self.y = x, y

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass


