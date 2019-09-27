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
    type = ""

    def __init__(self,location,type):

        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        
        self.type = type
        if self.type == 'save':
            savebutton.image = pygame.image.load('images/save.png').convert()
            print("saving button --LOADED")
        if self.type == 'load':
            savebutton.image = pygame.image.load('images/load.png').convert()
            print("loading button --LOADED")
        self.image = savebutton.image
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.topleft = location
 
            # Draw
        #pygame.draw.rect(self.image, color , [500, 50, width, height])
    def onclick(self):
        #if self.value%12 != 11:
        if self.type == "save":
            print("saving file")
        if self.type == "load":
            print("loading file")

