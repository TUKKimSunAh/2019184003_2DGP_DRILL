# class Star:
#     x = 100
#
#     def change():
#         x = 200
#         print('x is',x)
#
# print('x IS ', Star.x)
# Star.change()
#
# star = Star()
# star.change()

class Player:
    type = 'Player'

    def __init__(self):
        self.x = 100

    def where(self):
        print(self.x)

player = Player()
Player.where(player)