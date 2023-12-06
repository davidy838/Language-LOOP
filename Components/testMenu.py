import pygame
import sys
from doSpeakingTest import doSpeakingTest

from doTest import doTest
from speech import doSpeechPractice

def test_menu():
    pygame.init()

    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Pygame Vocabulary Game')

    font = pygame.font.Font(None, 36)

    # Define buttons with wider width
    button_width = 300
    button_height = 50
    button_x = (width - button_width) // 2  # Center the button

    button_pinyin = pygame.Rect(button_x, 200, button_width, button_height)
    button_speaking = pygame.Rect(button_x, 300, button_width, button_height)
    button_main = pygame.Rect(button_x, 400, button_width, button_height)  # New button for main


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_pinyin.collidepoint(event.pos):
                    doTest("module1")
                elif button_speaking.collidepoint(event.pos):
                    doSpeakingTest("module1")
                elif button_main.collidepoint(event.pos):
                    from Map.MainMap import main1
                    main1(1)  # Call main function

        screen.fill((255, 255, 255))

        # Draw buttons
        pygame.draw.rect(screen, (0, 0, 255), button_pinyin)
        pygame.draw.rect(screen, (0, 0, 255), button_speaking)
        pygame.draw.rect(screen, (0, 0, 255), button_main)  # Draw the main button


        # Add text to buttons
        text_pinyin = font.render('Practice Pinyin', True, (255, 255, 255))
        text_speaking = font.render('Practice Speaking', True, (255, 255, 255))
        text_main = font.render('Main Menu', True, (255, 255, 255))  # Text for the main button
        screen.blit(text_pinyin, (button_pinyin.x + 20, button_pinyin.y + 10))
        screen.blit(text_speaking, (button_speaking.x + 10, button_speaking.y + 10))
        screen.blit(text_main, (button_main.x + 20, button_main.y + 10))  # Place text on the main button

        pygame.display.flip()

    pygame.quit()
    sys.exit()
