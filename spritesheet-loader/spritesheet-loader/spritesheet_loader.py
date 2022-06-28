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

#grab the frame from the spritesheet (w/h of sheet,max row/col of sheet, frame row/col, scaled, color is transparent)
def get_frame(sheet,row,col,width,height,max_col,max_row,scale,color):
    image = pygame.Surface(((width//max_col),(height//max_row))).convert_alpha()  #create surface the size of a frame (sheet size divided by rows/cols) (using int division)
    image.blit(sheet,(0,0),((col * (width//max_col)),(row * (height//max_row)),(width//max_col), (height//max_row)))  #display the area (starting 0,0 to w,h) at 0,0
    image = pygame.transform.scale(image,((width//max_col) * scale,(height//max_row) * scale))  #scale image
    image.set_colorkey(color)  #set transparency
    return image

#initialize game variables
is_game_over = False  #moved this to game class last time, in game loop method
rows = 4  #rows in fox spritesheet
cols = 4  #cols in fox spritesheet
frames = []  #empty list for frame images
sheet_width = 384  #width of fox spritesheet
sheet_height = 384  #height of fox spritesheet

#initilize display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  #moved this to game class last time
pygame.display.set_caption("Spritesheet Loader")  #moved this to game class last time
spritesheet_image = pygame.image.load("Fox_idle.png").convert_alpha()  #load spritesheet image

for row in range(rows):
    for col in range(cols):
        frames.append(get_frame(spritesheet_image,row,col,sheet_width,sheet_height,rows,cols,1,BLACK))  #grab the frame from spritesheet

#game loop
#moved this to game class last time, in game loop method
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