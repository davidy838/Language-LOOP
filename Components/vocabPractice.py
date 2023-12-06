
import random
import pygame
import sys
import Map.MainMap
import database
import Components.player as player


def correctAnswer(random, side):
    if random % 2 == 0 and side == 0:  # correct on the left
        print("Correct")
        return True
    elif random % 2 != 0 and side == 1:  # correct on the right
        print("Correct")
        return True
    else:
        print("Incorrect")
        return False

def doVocabPractice(module):
    # Initialize Pygame
    pygame.init()

    # Set up the screen dimensions
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (200, 200, 200)
    BLUE = (173, 216, 230)

    # my variables
    img_width = 200
    img_height = 200
    numWordSeen = 0
    numCorrect = 0
    dictionary = database.my_map[module]
    practiceTime = False
    leftPos = (screen_width // 2 - 100, 450)
    rightPos = (screen_width // 2 + 100, 450)

    # Font initialization
    font = pygame.font.Font(None, 36)
    font1 = pygame.font.Font(None, 64)

    # Function to create a button
    def draw_button(x, y, width, height, text, button_color, text_color):
        pygame.draw.rect(screen, button_color, (x, y, width, height))

        text_surface = font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
        screen.blit(text_surface, text_rect)

    def display_data():
        # Fill the screen with a color (e.g., white)
        screen.fill((255, 255, 255))

        # Create a text surface
        text_surface = font.render(dictionary[numWordSeen % 5].english, True, (0, 0, 0))  # Data passed to the function
        text_surface2 = font.render(dictionary[numWordSeen % 5].pinyin, True, (0, 0, 0))
        text_surface1 = font1.render("Vocabulary Practice", True, (0, 0, 0))

        # Position the text on the screen
        text_rect = text_surface.get_rect(center=(screen_width // 2 - 100, 450))
        text_rect1 = text_surface1.get_rect(center=(screen_width // 2, 60))
        text_rect2 = text_surface2.get_rect(center=(screen_width // 2 + 100, 450))

        # Draw the text onto the screen
        screen.blit(text_surface, text_rect)
        screen.blit(text_surface1, text_rect1)
        screen.blit(text_surface2, text_rect2)

        # Draw buttons
        draw_button(600, 500, 200, 50, "Next", GRAY, BLACK)
        if numWordSeen >= 4:
            draw_button(600, 550, 200, 50, "Test Me", BLUE, BLACK)

        # Display images
        try:
            image = pygame.image.load(dictionary[numWordSeen % 5].picture)  # Replace with the image file path
            image1 = pygame.image.load(dictionary[numWordSeen % 5].character)
        except pygame.error as e:
            print(f"Unable to load image: {e}")
            sys.exit()
        scaled_image = pygame.transform.scale(image, (img_width, img_height))
        scaled_image1 = pygame.transform.scale(image1, (img_width, img_height))
        screen.blit(scaled_image, (screen_width/2-200, screen_height/2-100))
        screen.blit(scaled_image1, (screen_width/2, screen_height/2-100))

    def display_test():
        screen.fill((255, 255, 255))
        text_surface1 = font1.render("Vocabulary Practice", True, (0, 0, 0))
        text_rect1 = text_surface1.get_rect(center=(screen_width // 2, 60))
        screen.blit(text_surface1, text_rect1)

        testing = True
        numCorrect = 0
        lock = True

        while testing:
            if numCorrect >= 5:
                draw_button(600, 550, 200, 50, "Done", BLUE, BLACK)

            if lock:
                randomInt = random.randint(0, 4)
                randomInt2 = (randomInt + random.randint(1, 4)) % 5
                print(randomInt)

                try:
                    image1 = pygame.image.load(dictionary[randomInt].character)
                except pygame.error as e:
                    print(f"Unable to load image: {e}")
                    sys.exit()
                scaled_image1 = pygame.transform.scale(image1, (img_width, img_height))
                screen.blit(scaled_image1, (screen_width/2 - 100, screen_height/2-100))

                # The two options
                if randomInt % 2 == 0:  # correct on the left
                    draw_button(screen_width // 2 - 200, 450, 200, 50, dictionary[randomInt].pinyin, GRAY, BLACK)
                    draw_button(screen_width // 2, 450, 200, 50, dictionary[randomInt2].pinyin, GRAY, BLACK)
                    print("L correct")
                else:
                    draw_button(screen_width // 2 - 200, 450, 200, 50, dictionary[randomInt2].pinyin, GRAY, BLACK)
                    draw_button(screen_width // 2, 450, 200, 50, dictionary[randomInt].pinyin, GRAY, BLACK)
                    print("R correct")

                pygame.display.flip()

                lock = False

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    button_left = pygame.Rect(screen_width // 2 - 200, 450, 200, 50)
                    button_right = pygame.Rect(screen_width // 2, 450, 200, 50)
                    button_done = pygame.Rect(600, 550, 200, 50)
                    if button_left.collidepoint(mouse_pos):
                        if correctAnswer(randomInt, 0):
                            numCorrect += 1
                        # print("Left Button clicked!")
                        pygame.display.flip()
                        lock = True
                    if button_right.collidepoint(mouse_pos):
                        if correctAnswer(randomInt, 1):
                            numCorrect += 1
                        # print("Right Button clicked")
                        pygame.display.flip()
                        lock = True
                    if button_done.collidepoint(mouse_pos):
                        testing = False

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                button_next = pygame.Rect(600, 500, 200, 50)  # Define button rectangle coordinates and size
                button_done = pygame.Rect(600, 550, 200, 50)
                if button_next.collidepoint(mouse_pos):
                    print("Next Button clicked!")  # Functionality when the button is clicked
                    numWordSeen += 1
                elif button_done.collidepoint(mouse_pos):
                    print("Done Button clicked")
                    if practiceTime:
                        running = False
                    practiceTime = True

        screen.fill(WHITE)

        # Draw buttons and show data
        if practiceTime:
            display_test()
            from Map.MainMap import main1
            main1(0)

        else:
            display_data()

        pygame.display.flip()

    # Quit Pygame properly
    pygame.quit()
    sys.exit()
