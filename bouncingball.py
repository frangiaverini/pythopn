import pygame

# initialize all modules in pygame
pygame.init()

# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# set wisth and height of the screen (x, y)

size = (700, 500)

screen = pygame.display.set_mode(size)

# include a caption on screen 
pygame.display.set_caption("My Fabulous Game")

# loop until user clicks "close" button
done = False 

#clock is used to manage how fast your screen updates
clock = pygame.time.Clock()

#----Main Loop----#
while not done:
    #___Main Event Loop___#	
	for event in pygame.event.get():
	    if event.type == pygame.QUIT:
                done = True
		#game logic goes here#
		
		
		#screen clearing code goes here#
		
		
		#here, we clear the screen to white. Don't put the drawing above this, or they will be erased by this command
		
		
		#if you want a backgound image, replece this clear with blit'ing the backgound image using pygame.blit()
                screen.fill(WHITE)
		
		
		#-----drawing code-----#
		#pygame.rect(surface, color, start, end, width = 1)
		#draw a red diagonal line
                pygame.draw.rect(screen, RED, (0, 0, 700, 500), 2)
		
		#-----Update screen with drawing----#
                pygame.display.flip()
		#pygame.display.update(rect)
                pygame.draw.rect(r)	
	
		#-----limit to 60 frames per second-----
                clook.tick(60)
		
		
pygame.quit()
exit()
		
		
		
		
		
