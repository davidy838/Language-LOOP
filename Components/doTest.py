import pygame
import sys
from Components.word import Word
from database import my_map

def draw_input_box(screen, input_box, color, text=''):
    font = pygame.font.Font(None, 32)
    txt_surface = font.render(text, True, color)
    screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
    pygame.draw.rect(screen, color, input_box, 2)

def draw_message_box(screen, message, width, height):
    font = pygame.font.Font(None, 50)
    text_surface = font.render(message, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(width // 2, height // 2))

    message_box_rect = pygame.Rect(width // 2 - 150, height // 2 - 50, 300, 100)
    pygame.draw.rect(screen, (255, 255, 255), message_box_rect)
    pygame.draw.rect(screen, (0, 0, 0), message_box_rect, 2)  # Border

    screen.blit(text_surface, text_rect)
    

def load_image(path):
    try:
        image = pygame.image.load(path)
        return image
    except pygame.error as e:
        print(f"Cannot load image: {path}. Error: {e}")
        raise SystemExit(e)

def doTest(module):
    pygame.init()

    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Pygame Vocabulary Test')

    input_box = pygame.Rect(300, 500, 200, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''

    # Load words from my_map
    words = my_map[module]
    current_index = 0
    current_word = words[current_index]
    image = load_image(current_word.character)

    message = ""
    show_message = False
    message_display_time = 0  # Time for which the message is displayed

    # exit button
    exit_button = pygame.Rect(50, 550, 100, 40)  # Adjust size and position as needed

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                elif exit_button.collidepoint(event.pos):
                    from Map.MainMap import main1
                    main1(1)
                    return
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        if text == current_word.pinyin:
                            message = "Congrats"
                            show_message = True
                            message_display_time = pygame.time.get_ticks()  # Record the time when the message is shown
                        else:
                            message = "Try again"
                            show_message = True
                            message_display_time = pygame.time.get_ticks()  # Record the time when the message is shown
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((255, 255, 255))
        if not show_message:
            screen.blit(image, (width // 2 - image.get_width() // 2, 100))

        draw_input_box(screen, input_box, color, text)

        if show_message:
            draw_message_box(screen, message, width, height)
            # Check if 1 second has passed since the message was shown
            if pygame.time.get_ticks() - message_display_time > 1000:
                if message == "Congrats":
                    current_index += 1
                    if current_index < len(words):
                        current_word = words[current_index]
                        image = load_image(current_word.character)
            
                    else:
                        message = "End of vocabulary list"
                        pygame.time.wait(300)
                        from Components.testMenu import test_menu
                        test_menu()
                        return
                show_message = False  # Hide the message for the next word or after "Try again"

        # Draw the exit button
        pygame.draw.rect(screen, (200, 200, 200), exit_button)
        font = pygame.font.Font(None, 32)
        text_surface = font.render('Exit', True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=exit_button.center)
        screen.blit(text_surface, text_rect)

        pygame.display.flip()

    pygame.quit()
    sys.exit()