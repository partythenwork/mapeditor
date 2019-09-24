import pygame
import constants

class Block(pygame.sprite.Sprite):

    mapx = 0
    mapy = 0
    value = 0 #0 to 63
    # Constructor. Pass in the color of the block,
    # and its x and y position

		   
    def __init__(self,sheet):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)
		
       self.image = sheet.get_image(0,0,constants.TILE_WIDTH,constants.TILE_HEIGHT)
       self.rect = self.image.get_rect()

    def change_tile(self,sheet):
        #if self.value%12 != 11:
        self.value += 1
        if self.value >= 96:
            self.value = 0
        self.display_tile(sheet)
       
       
    def display_tile(self,sheet):
       #calculate where on spritesheet to get image
        x = (self.value%12)*constants.TILE_WIDTH
        y = int(self.value/12)*constants.TILE_HEIGHT
        self.image = sheet.get_image(x,y,constants.TILE_WIDTH,constants.TILE_HEIGHT)