# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()
import sys

import time

# Initialize the clock
clock = pygame.time.Clock()
# Define variables for timing
last_time = pygame.time.get_ticks()
timer_interval = 1000  # Timer interval in milliseconds (1 second)

# Letter functionality 
lettersUsed = 0

# Open the text file for reading
with open('Books\Cat_In_The_Hat.txt', 'r') as file:
    # Read the entire content of the file
    content = file.readline().rstrip()

rightChar = 'none'

# Set up txt colors
black = (0,0,0)
blue = (145,182,255)

def newLetter():
    global lettersUsed
    global rightChar

    if lettersUsed < len(content):
        try:
            rightChar = content[lettersUsed]
            new = biggestFont.render(rightChar, True, black)
            screen.blit(new, (225, 200))
        except Exception as e:
            print("Error rendering letter:", e)

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Naming 
pygame.display.set_caption('Dr.Suess Cat in the Hat Game')

# Load the font
fontLink = 'Fonts\Seuss-G4Ra.ttf'
font = pygame.font.Font(fontLink, 32)
smallFont = pygame.font.Font(fontLink, 18)
bigFont = pygame.font.Font(fontLink, 60)
biggestFont = pygame.font.Font(fontLink, 150)

#introduce parameters at their original number
sec = 45

# Setup function
def setup():
    # Fill the background with black
    screen.fill(blue)

    intro_text = font.render(f'Type the letter. Lives: {lives}', True, black) 
    rules_text = smallFont.render("Ok to make mistakes, as long as you get it in time", True, black)
    help_text = smallFont.render("Follow along with Cat in The Hat! as you play", True, black)

    screen.blit(intro_text, (95,10))
    screen.blit(rules_text, (55,40))
    screen.blit(help_text, (75,60))

    newLetter()
    timerDraw()


#Timer
def findInitSec():
    global lettersUsed
    global sec

    if lettersUsed > 750:
        sec = 5
    elif lettersUsed > 500:
        sec = 10
    elif lettersUsed > 250:
        sec = 15
    elif lettersUsed > 100:
        sec = 20
    elif lettersUsed > 15:
        sec = 30
    else:
        sec = 45

def timerDraw():
    global sec 

    timer_text = bigFont.render(f"Time left: {sec} seconds", True, black)
    screen.blit(timer_text, (0,400))

def timer():
    global lives
    global lettersUsed
    global sec
    
    sec -= 1  
    
    if sec <= 0:
        lives -= 1
        advance()



def advance():
    global lettersUsed

    lettersUsed += 1
    print(rightChar)
    findInitSec()

# Run until life out
lives = 3
running = True
while running and lives > 0:
    # Calculate elapsed time since the last frame
    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - last_time
    last_time = current_time

    # Call setup function before rendering the letter
    setup()
    #newLetter()
    timer()
    
    # Flip the display
    pygame.display.flip()

    clock.tick(1)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Check if the pressed key matches the value of rightChar
            if event.unicode == rightChar: advance()


    # Check if it's time to perform a timed action (e.g., update timer)
    if elapsed_time >= timer_interval:
        # Update the timer or perform other timed actions here
        timer()

# Done! Time to quit.
pygame.quit()
sys.exit()
