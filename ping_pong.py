from pygame import *

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("PING PONG")
background = transform.scale(image.load("realistic-table-tennis-background_52683-45882.jpg"), (win_width, win_height))
ball_pingpong = '544410.jpeg'

class GameSprite(sprite.Sprite):
  
   def __init__(self, player_image, player_x, player_y, player_speed):
       super().__init__()
       
       self.image = transform.scale(image.load(player_image), (65, 65))
       self.speed = player_speed

      
        
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
    
 

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
        window.blit(self.image, (self.rect.x, self.rect.y))
    def updateL(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= 3
        if key_pressed[K_DOWN] and self.rect.y < win_height - 220:
            self.rect.y += 3
    def updateR(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= 3
        if key_pressed[K_s] and self.rect.y < win_height - 220:
            self.rect.y += 3

wall1 = Wall(16, 213, 53, 15, 220, win_width - 50, 120)
wall2 = Wall(16, 213, 53, 15, 220, 50, 120)
#wall1.draw_wall()
#wall2.draw_wall()
ball = GameSprite(ball_pingpong, 200, 0, 2)
game = True
FPS = 60

speed_x = 3
speed_y = 3
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background, (0, 0))
    

    wall1.updateL()
    wall2.updateR()
    
    wall1.draw_wall()
    wall2.draw_wall()

    ball.reset()
    ball.rect.x += speed_x
    ball.rect.y += speed_y


    if sprite.collide_rect(ball, wall1) or sprite.collide_rect(ball, wall2):
        speed_x *= - 1

    if ball.rect.y > win_height - 50 or ball.rect.y < 0:
        speed_y *= - 1
    
    display.update()
