from pygame import *

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("PING PONG")
background = transform.scale(image.load("realistic-table-tennis-background_52683-45882.jpg"), (win_width, win_height))

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_width, wall_height, wall_x, wall_y):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height

        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.x))


wall1 = Wall(166, 219, 8, 15, 220, 180, 80)
wall2 = Wall(255, 0, 1, 15, 430, 150, 150)
wall1.draw_wall()
wall2.draw_wall()

game = True
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    wall1.draw_wall()
    wall2.draw_wall()

    window.blit(background, (0, 0))
    display.update()
