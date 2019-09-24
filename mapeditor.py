import pygame
import random
from pygame.locals import *
from sys import exit
import spritesheet

class Block(pygame.sprite.Sprite):

    mapx = 0
    mapy = 0
    value = 0 #0 to 63
    # Constructor. Pass in the color of the block,
    # and its x and y position

		   
    def __init__(self,ss):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)
		
       self.image = ss.get_image(0,0,32,32)
       self.rect = self.image.get_rect()

    def change_tile(self,ss):
        if self.value%12 != 11:
            self.value += 1
        self.display_tile(ss)
       
       
    def display_tile(self,ss):
       #calculate where on spritesheet to get image
        x = (self.value%12)*TILE_WIDTH
        y = int(self.value/12)*TILE_HEIGHT
        self.image = ss.get_image(x,y,TILE_WIDTH,TILE_HEIGHT)


pygame.init()

#screen dimensions
screen_width=800
screen_height=600
map_WIDTH = 10
map_HEIGHT = 5
TILE_WIDTH = 32
TILE_HEIGHT = 32
map_startx = 100
map_starty = 200

# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE =  (  0,   0, 255)

screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
caption = pygame.display.set_caption('Map Editor')
font = pygame.font.SysFont("arial", 17);
font_height = font.get_linesize()

#load a spritesheet -- must come after screen first
farmsprites = spritesheet.SpriteSheet("crops_fields.png")

#All blocks are here
all_sprites_list = pygame.sprite.Group()

#initialize map
map = [[0 for i in range(map_WIDTH)] for j in range(map_HEIGHT)]
#create a block and add to all_sprites_list group
y=0
for row in map:
    x=0
    for element in row:
        value =  random.randrange(0,96)
        map[y][x] = value
        square = Block(farmsprites)
        square.value = value
        square.rect.x = x*TILE_WIDTH + map_startx
        square.rect.y = y*TILE_HEIGHT + map_starty
        square.display_tile(farmsprites)
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
                    sprite.change_tile(farmsprites)
                    print("you clicked on tile at ",sprite.mapx,",",sprite.mapy," at mouse:",mouse_pos)
    screen.fill((255, 255, 255))
    
    x, y = pygame.mouse.get_pos()
    click= pygame.mouse.get_pressed()
    
    # Draw all the spites
    all_sprites_list.draw(screen)
    
    text_surface = font.render("x coordinate : " + str(x) + " y coordinate : " + str(y), True, (0,0,0))
    screen.blit(text_surface, (10, font_height))
    pygame.display.update()