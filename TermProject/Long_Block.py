from pico2d import *
import Game_World


class Long_Block:
    image = None

    def __init__(self, x, y):
        if Long_Block.image == None:
            Long_Block.image = load_image('Long_Block.png')
        self.width, self.height = 762, 90
        self.x, self.y = x, y

    def get_bb(self):
        return self.x - 762 / 2, self.y - 90 / 2, self.x + 762 / 2, self.y + 90 / 2

    def update(self):
        if self.x < 0 or self.x > 800:
            Game_World.remove_object(self)
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
