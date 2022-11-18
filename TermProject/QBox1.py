from pico2d import *
import Game_World


class QBox1:

    def __init__(self, x, y):
        self.CheckState = 1
        self.width, self.height = 34, 34
        self.x, self.y = x, y

        if self.CheckState == 1:
                self.image = load_image('QBox1.png')


    def get_bb(self):
        return self.x - 15, self.y - 15, self.x + 15, self.y + 15

    def update(self):
        if self.CheckState > 1:
            self.image = load_image('QBox_Die.png')
            
        if self.x < 0 or self.x > 800:
            Game_World.remove_object(self)
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
