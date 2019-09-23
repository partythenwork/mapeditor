import pygame
import random
from pygame.locals import *
from sys import exit

class Block(pygame.sprite.Sprite):

    mapx = 0
    mapy = 0
    value = 0
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.Surface([width, height])
       self.image.fill(color)

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()

    def change_tile(self):
        self.value += 1
        if self.value > 3:
            self.value = 0
        self.display_tile()
       
       
    def display_tile(self):
        if self.value == 1:
            self.image.fill(RED)
        elif self.value == 2:
            self.image.fill(GREEN)
        elif self.value == 3:
            self.image.fill(BLUE)
        else:
            self.image.fill(BLACK)


pygame.init()

#screen dimensions
screen_width=800
screen_height=600
map_WIDTH = 10
map_HEIGHT = 5
TILE_WIDTH = 50
TILE_HEIGHT = 25
map_startx = 100
map_starty = 200

# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE =  (  0,   0, 255)

screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
caption = pygame.display.set_caption('Mouse Test')
font = pygame.font.SysFont("arial", 17);
font_height = font.get_linesize()

#All blocks are here
all_sprites_list = pygame.sprite.Group()

#initialize map
map = [[0 for i in range(map_WIDTH)] for j in range(map_HEIGHT)]
#create a block and add to all_sprites_list group
y=0
for row in map:
    x=0
    for element in row:
        value = random.randrange(0,4)
        map[y][x] = value
        square = Block(BLACK,TILE_WIDTH,TILE_HEIGHT)
        square.value = value
        square.rect.x = x*TILE_WIDTH + map_startx
        square.rect.y = y*TILE_HEIGHT + map_starty
        square.display_tile()
        square.mapx=x
        square.mapy=y
        all_sprites_list.add(square)
        x+=1
    y+=1
        


#main loop 
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for sprite in all_sprites_list:
                if sprite.rect.collidepoint(x,y):
                    sprite.change_tile()
                    print("you clicked on tile at ",sprite.mapx,",",sprite.mapy," at mouse:",mouse_pos)
    screen.fill((255, 255, 255))
    
    x, y = pygame.mouse.get_pos()
    click= pygame.mouse.get_pressed()
    
    # Draw all the spites
    all_sprites_list.draw(screen)
    
    text_surface = font.render("x coordinate : " + str(x) + " y coordinate : " + str(y), True, (0,0,0))
    screen.blit(text_surface, (10, font_height))
    pygame.display.update()
