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

#classes
class Spritesheet():
    def __init__(self,image):
        self.sheet = image  #spritesheet image

    #grab individual frame from the spritesheet (w/h of sheet,max row/col of sheet, frame row/col, scaled, color is transparent)
    def get_frame(self,row,col,width,height,cols,rows,scale,color):
        image = pygame.Surface(((width//cols),(height//rows))).convert_alpha()  #create surface the size of a frame (sheet size divided by rows/cols) (using int division)
        image.blit(self.sheet,(0,0),((col * (width//cols)),(row * (height//rows)),(width//cols), (height//rows)))  #display the area (starting 0,0 to w,h) at 0,0
        image = pygame.transform.scale(image,((width//cols) * scale,(height//rows) * scale))  #scale image
        image.set_colorkey(color)  #set transparency
        return image

    #grab all the frames from the spreadsheet (w/h of sheet, max row/col of sheet, scaled, color is transparent)
    def get_frames(self,width,height,cols,rows,scale,color):
        frames = []  #empty list for frame images
        for row in range(rows):
            for col in range(cols):
                frames.append(self.get_frame(row,col,width,height,cols,rows,scale,color))  #grab the frame from spritesheet
        return frames
    
#initialize game variables
is_game_over = False  #moved this to game class last time, in game loop method
rows = 4  #rows in fox spritesheet
cols = 4  #cols in fox spritesheet
sheet_width = 384  #width of fox spritesheet
sheet_height = 384  #height of fox spritesheet
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  #moved this to game class last time
spritesheet_image = pygame.image.load("Fox_idle.png").convert_alpha()  #load spritesheet image
spritesheet = Spritesheet(spritesheet_image)  #instantiate spritesheet object
frames = spritesheet.get_frames(sheet_width,sheet_height,cols,rows,1,BLACK)  #get all frames from spritesheet

#initilize display
pygame.display.set_caption("Spritesheet Loader")  #moved this to game class last time

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