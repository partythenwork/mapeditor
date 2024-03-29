import pygame
import random
from pygame.locals import *
from sys import exit
import spritesheet
import Block
import constants

def printmap(a,option=0):
    string=""
    for i in range(len(a)):
        for j in range(len(a[i])):
            if j > 0:
                string += "-"
            valuestring = str(a[i][j])
            if len(valuestring) < 2:
                valuestring = "0"+valuestring     
            string += valuestring
        string += "\n"
    if option == 1:
        file = open("data.txt","w")
        file.write(string)
        file.close()
    
    print(string)
    
def loadmap(a,option=0):
    file = open("data.txt","r")
    lines = file.readlines()
    for line in lines:
        line.rstrip() #remove all \n and trailing whitespaces
        elements = line.split("-")
        for string in elements:
            value = int(string)
            print(value)
        print()
    file.close()
            

pygame.init()

screen = pygame.display.set_mode((constants.screen_width, constants.screen_height), 0, 32)
caption = pygame.display.set_caption('Map Editor')
font = pygame.font.SysFont("arial", 17);
font_height = font.get_linesize()

#load a spritesheet -- must come after screen first
farmsprites = spritesheet.SpriteSheet('images/crops_fields.png')

#All blocks are here
all_sprites_list = pygame.sprite.Group()
#all control sprites are here
control_sprites_list = pygame.sprite.Group()

#initialize map
map = [[0 for i in range(constants.map_WIDTH)] for j in range(constants.map_HEIGHT)]
#create a block and add to all_sprites_list group
y=0
for row in map:
    x=0
    for element in row:
        value =  random.randrange(0,96)
        map[y][x] = value
        square = Block.Block(farmsprites,constants.TILE_WIDTH,constants.TILE_HEIGHT)
        square.value = value
        square.rect.x = x*square.width + constants.map_startx
        square.rect.y = y*square.height + constants.map_starty
        square.display_tile(farmsprites)
        square.mapx=x
        square.mapy=y
        all_sprites_list.add(square)
        x+=1
    y+=1
        
#after loading map load save icon

load_icon = Block.savebutton([500,200],"load")
control_sprites_list.add(load_icon)

save_icon = Block.savebutton([500,50],"save")
control_sprites_list.add(save_icon)

#main loop 
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                printmap(map,0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for sprite in all_sprites_list:
                if sprite.rect.collidepoint(x,y):
                    sprite.onclick(farmsprites)
                    map[sprite.mapy][sprite.mapx] = sprite.value
                    print("you clicked on tile at ",sprite.mapx,",",sprite.mapy," at mouse:",mouse_pos," changing value to:",sprite.value)
            for sprite in control_sprites_list:
                if sprite.rect.collidepoint(x,y):
                    sprite.onclick()
                    if sprite.type == "save":
                        printmap(map,1)
                    elif sprite.type == "load":
                        loadmap(map,1)

    screen.fill((255, 255, 255))
    
    x, y = pygame.mouse.get_pos()
    click= pygame.mouse.get_pressed()
    
    # Draw all the spites
    all_sprites_list.draw(screen)
    control_sprites_list.draw(screen)
    
    text_surface = font.render("x coordinate : " + str(x) + " y coordinate : " + str(y), True, (0,0,0))
    screen.blit(text_surface, (10, font_height))
    pygame.display.update()