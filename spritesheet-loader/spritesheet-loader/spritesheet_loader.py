# Spritesheet Loader
# Loads images from a spritesheet for use with my games

#imports
import pygame

#initilize game engine
pygame.init()

#constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GREY = (50,50,50)
BLACK = (0,0,0)

#functions
#grab the frame from the spritesheet (w/h of frame on sheet, scaled, color is transparent)
def get_frame(sheet,width,height,scale,color):
    image = pygame.Surface((width,height)).convert_alpha()  #create surface the size of a frame
    image.blit(sheet,(0,0),(0,0,width, height))  #display the area (starting 0,0 to w,h) at 0,0
    image = pygame.transform.scale(image,(width * scale,height * scale))  #scale image
    image.set_colorkey(color)  #set transparency
    return image

#initilize display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  #moved this to game class last time
pygame.display.set_caption("Spritesheet Loader")  #moved this to game class last time
spritesheet_image = pygame.image.load("Fox_idle.png").convert_alpha()  #load spritesheet image
frame = get_frame(spritesheet_image,96,96,2,BLACK)  #grab the 1st frame from spritesheet

#initialize game variables
is_game_over = False  #moved this to game class last time, in game loop method

#game loop
#moved this to game class last time, in game loop method
while not is_game_over:
    
    #clear screen
    screen.fill(GREY)

    #display frame
    screen.blit(frame, (0,0))
    
    #event handler
    for event in pygame.event.get():
        #game quit
        if event.type == pygame.QUIT:
            is_game_over = True

        #update display
        pygame.display.update()

#quit game
pygame.quit()