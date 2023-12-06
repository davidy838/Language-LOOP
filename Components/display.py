import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants for colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the window
window_size = (400, 300)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Pygame Window')

# Font setup
font = pygame.font.Font(None, 36)

# Word variable placeholder
word_variable = "Display Word Here"

# Function to display text on the screen
def display_text(text):
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(window_size[0] // 2, window_size[1] // 2))
    screen.blit(text_surface, text_rect)

# Main loop
running = True
while running:
    screen.fill(WHITE)
    display_text(word_variable)

    # Exit button at the top right
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            if 0 <= x <= 50 and 0 <= y <= 30:  # Exit button location
                running = False

    # Repeat button
    pygame.draw.rect(screen, BLACK, (20, 50, 100, 40))  # Repeat button rectangle
    repeat_text = font.render("Repeat", True, WHITE)
    screen.blit(repeat_text, (30, 60))

    # Next button at the bottom left
    pygame.draw.rect(screen, BLACK, (20, 250, 100, 40))  # Next button rectangle
    next_text = font.render("Next", True, WHITE)
    screen.blit(next_text, (30, 260))

    pygame.display.flip()

# Quit Pygame properly
pygame.quit()
sys.exit()