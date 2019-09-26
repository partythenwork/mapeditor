import pygame

class Block(pygame.sprite.Sprite):

    mapx = 0
    mapy = 0
    value = 0 #0 to 63
    # Constructor. Pass in the color of the block,
    # and its x and y position
    width = 0
    height = 0

		   
    def __init__(self,sheet,width,height):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)
       self.width = width
       self.height = height
		
       self.image = sheet.get_image(0,0,width,height)
       self.rect = self.image.get_rect()

    def onclick(self,sheet=None):
        #if self.value%12 != 11:
        self.value += 1
        if self.value >= 96:
            self.value = 0
        self.display_tile(sheet)
       
       
    def display_tile(self,sheet):
       #calculate where on spritesheet to get image
        x = (self.value%12)*self.width
        y = int(self.value/12)*self.height
        self.image = sheet.get_image(x,y,self.width,self.height)

        
class savebutton(pygame.sprite.Sprite):
    image = None

    def __init__(self,location):

        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        
        if savebutton.image is None:
            savebutton.image = pygame.image.load('floppy-icon.png').convert()
        self.image = savebutton.image
        self.rect = self.image.get_rect()
        self.rect.topleft = location
 
            # Draw
        #pygame.draw.rect(self.image, color , [500, 50, width, height])
    def onclick(self):
        #if self.value%12 != 11:
        print("saving file");

