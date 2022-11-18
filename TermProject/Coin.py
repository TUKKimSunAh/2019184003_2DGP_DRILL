from pico2d import *
import Game_World


class Coin:
    image = None

    def __init__(self, x, y):
        if Coin.image == None:
            Coin.image = load_image('Coin.png')

        self.frame = 0
        self.width, self.height = 17, 30
        self.x, self.y = x, y

    def get_bb(self):
        return self.x - 17, self.y - 15, self.x + 17, self.y + 15

    def update(self):
        self.frame = (self.frame + 3) % 4
        if self.x < 0 or self.x > 800:
            Game_World.Remove_Object(self)
        pass

    def draw(self):
        self.image.clip_draw(self.frame * 17, 0, 17, 30, self.x, self.y)
