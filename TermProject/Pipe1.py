from pico2d import *
import Game_World


class Pipe1:
    image = None

    def __init__(self, x, y):
        if Pipe1.image == None:
            Pipe1.image = load_image('Pipe1.png')
        self.width, self.height = 54, 81
        self.x, self.y = x, y

    def get_bb(self):
        return self.x - 27, self.y - 81/2, self.x + 27, self.y + 81/2


    def update(self):
        if self.x < 0 or self.x > 800:
            Game_World.remove_object(self)
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
