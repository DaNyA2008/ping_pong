from pygame import *

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("PING PONG")
background = transform.scale(image.load("realistic-table-tennis-background_52683-45882.jpg"), (win_width, win_height))

game = True
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background, (0, 0))
    display.update()
        
