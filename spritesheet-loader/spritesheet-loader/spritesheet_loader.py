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
def get_frame(sheet,frame,width,height,scale,color):
    image = pygame.Surface((width,height)).convert_alpha()  #create surface the size of a frame
    image.blit(sheet,(0,0),((frame * width),0,width, height))  #display the area (starting at frame # * width of frame, and only in a row (y=0) to w,h) at 0,0
    image = pygame.transform.scale(image,(width * scale,height * scale))  #scale image
    image.set_colorkey(color)  #set transparency
    return image

#initilize display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  #moved this to game class last time
pygame.display.set_caption("Spritesheet Loader")  #moved this to game class last time
spritesheet_image = pygame.image.load("Fox_idle.png").convert_alpha()  #load spritesheet image
frame_0 = get_frame(spritesheet_image,0,96,96,2,BLACK)  #grab the 1st frame from spritesheet
frame_1 = get_frame(spritesheet_image,1,96,96,2,BLACK)  #grab the 2nd frame from spritesheet
frame_2 = get_frame(spritesheet_image,2,96,96,2,BLACK)  #grab the 3rd frame from spritesheet

#initialize game variables
is_game_over = False  #moved this to game class last time, in game loop method

#game loop
#moved this to game class last time, in game loop method
while not is_game_over:
    
    #clear screen
    screen.fill(GREY)

    #display frames
    screen.blit(frame_0, (0,0))
    screen.blit(frame_1, (193,0))
    screen.blit(frame_2, (386,0))
    
    #event handler
    for event in pygame.event.get():
        #game quit
        if event.type == pygame.QUIT:
            is_game_over = True

        #update display
        pygame.display.update()

#quit game
pygame.quit()