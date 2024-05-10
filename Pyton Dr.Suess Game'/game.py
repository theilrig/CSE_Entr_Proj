# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

#import game_code

# Set up the drawing window
screen = pygame.display.set_mode([500, 700])

#Naming 
pygame.display.set_caption('Dr.Suess Cat in the Hat Game')

# Load the font
font = pygame.font.Font('Fonts\Seuss-G4Ra.ttf', 32)

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((145,182,255))


    intro_text = font.render('Type the letter you see', True, (0, 0, 0))  # Text color is white, background color is black
    screen.blit(intro_text, (95,10))  # Position the text at (100, 100)
    # Flip the display
    pygame.display.flip()
# Done! Time to quit.
pygame.quit()