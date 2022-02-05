#Student Name		William Zhu
#Student Number		101231064

#Importing necessary libraries
import pygame, random, sys

pygame.init()

#Declaring variables
numRed = int()
numGreen = int()
numBlue = int()
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
counter = int()

#Loading image and getting dimensions
image = pygame.image.load(sys.argv[1])
height = image.get_height()
width = image.get_width()

#Scaling dimensions
window = pygame.display.set_mode((round(width*(5/2)),round(height*(5/2))))

#Nested loop to draw new image
for x in range(1,width):
	for y in range(1,height):
		#Determining how many circles of each colour to draw
		colour = image.get_at((x,y))
		numRed = round(colour[0]/25.5)
		numGreen = round(colour[1]/25.5)
		numBlue = round(colour[2]/25.5)
		counter = 1
		#Drawing circles on new image
		while(True):
			if(counter <= numRed):
				pygame.draw.circle(window,red,(random.uniform(x*(5/2)-4,x*(5/2)),random.uniform(y*(5/2) - 4,y*(5/2))),1)
			if(counter <= numGreen):
				pygame.draw.circle(window,green,(random.uniform(x*(5/2) - 4,x*(5/2)),random.uniform(y*(5/2) - 4,y*(5/2))),1)
			if(counter <= numBlue):
				pygame.draw.circle(window,blue,(random.uniform(x*(5/2) - 4,x*(5/2)),random.uniform(y*(5/2) - 4,y*(5/2))),1)
			if((counter > numRed) and (counter > numGreen) and (counter > numBlue)): break
			counter += 1

pygame.display.update()
pygame.time.delay(10000)

