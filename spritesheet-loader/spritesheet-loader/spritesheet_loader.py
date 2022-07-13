# Spritesheet Loader
# Loads images from a spritesheet for use with my games
# by Sarah Pierce

#imports
import pygame
import spritesheet  #new spritesheet library

#initilize game engine
pygame.init()

#constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GREY = (50,50,50)
BLACK = (0,0,0)
    
#initialize game variables
is_game_over = False
rows = 4  #rows in fox spritesheet
cols = 4  #cols in fox spritesheet
sheet_width = 384  #width of fox spritesheet
sheet_height = 384  #height of fox spritesheet
crop = False  #crop the returned images
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
spritesheet_image = pygame.image.load("Fox_idle.png").convert_alpha()  #load spritesheet image
spritesheet = spritesheet.Spritesheet(spritesheet_image,sheet_width,sheet_height,rows,cols,crop)  #instantiate spritesheet object
frames = spritesheet.get_frames(1,BLACK)  #get all frames from spritesheet

#initilize display
pygame.display.set_caption("Spritesheet Loader")

#game loop
while not is_game_over:
    
    y = 0  #used to display images
    x = 0  #used to display images
    
    #clear screen
    screen.fill(GREY)

    #display frames
    for i in range(len(frames)):
        if (i != 0) and (i % 4 == 0):
            y += 1  #move down one line after 4
            x = 0  #reset to left after 4
        screen.blit(frames[i], ((sheet_width//cols)*x,(sheet_height//rows)*y))
        x += 1
    
    #event handler
    for event in pygame.event.get():
        #game quit
        if event.type == pygame.QUIT:
            is_game_over = True

        #update display
        pygame.display.update()

#quit game
pygame.quit()