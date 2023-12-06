from Components.word import Word
from Components.speechValidation import speechValidator
import speech_recognition as sr
from pygame import font
from Components.database import my_map

import pygame
import sys

BLACK = (0, 0, 0)
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.font.init()
custom_font = pygame.font.Font(None, 36)

def display_message(message):
    text_surface = custom_font.render(message, True, BLACK)
    text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height - 50))
    screen.blit(text_surface, text_rect)

def capture_audio():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Recording... (Say something)")
        audio = recognizer.listen(source)

    print("Recording stopped.")
    return audio


def doSpeechPractice(module):

    recognized_text = ""  # Initialize recognized text variable


    audio_files = []
    for word in my_map[module]: [
        audio_files.append(word.audio)


    ]
    word_files = []
    for word in my_map[module]: [
        word_files.append(word.chinese)


    ]
        
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
    dictionary = my_map[module]

    # Font initialization
    font = pygame.font.Font(None, 36)
    font1 = pygame.font.Font(None, 64)

    chinese_font_path = '/Users/davidyang/Desktop/Language LOOP/Components/msyh.ttf'  # Replace with the path to your Chinese font file
    chinese_font = pygame.font.Font(chinese_font_path, 36)  # You can adjust the size as needed


    #Play audio function
    def play_audio(file_path):
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
    
        

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
        text_surface1 = font1.render("Speech Practice", True, (0, 0, 0))

        # Position the text on the screen
        text_rect = text_surface.get_rect(center=(screen_width // 2 - 100, 450))
        text_rect1 = text_surface1.get_rect(center=(screen_width // 2, 60))
        text_rect2 = text_surface2.get_rect(center=(screen_width // 2 + 100, 450))

        # Draw the text onto the screen
        screen.blit(text_surface, text_rect)
        screen.blit(text_surface1, text_rect1)
        screen.blit(text_surface2, text_rect2)

        message_display_time = None

        if recognized_text:
            print(recognized_text)
            display_text = recognized_text[0] if recognized_text[0] == word_files[numWordSeen % 5] else recognized_text
            text_surface_recognized = chinese_font.render(display_text, True, BLACK)
            text_rect_recognized = text_surface_recognized.get_rect(center=(screen_width // 2, 550))
            screen.blit(text_surface_recognized, text_rect_recognized)

            if recognized_text[0] == word_files[numWordSeen % 5]:
                correct_msg = "Correct"
                text_surface_correct = font.render(correct_msg, True, BLACK)
                text_rect_correct = text_surface_correct.get_rect(left=text_rect_recognized.right + 10, centery=text_rect_recognized.centery)
                screen.blit(text_surface_correct, text_rect_correct)
                message_display_time = pygame.time.get_ticks()  # Record the time when the message is displayed
            else:
                incorrect_msg = "Incorrect"
                text_surface_incorrect = font.render(incorrect_msg, True, BLACK)
                text_rect_incorrect = text_surface_incorrect.get_rect(right=text_rect_recognized.left - 10, centery=text_rect_recognized.centery)
                screen.blit(text_surface_incorrect, text_rect_incorrect)
                message_display_time = pygame.time.get_ticks()  #

        # Draw buttons
        draw_button(600, 500, 200, 50, "Next", GRAY, BLACK)
        if numWordSeen >= 4:
            draw_button(600, 550, 200, 50, "Done", BLUE, BLACK)
        draw_button(600, 450, 200, 50, "Play Audio", GRAY, BLACK)
        draw_button(600, 400, 200, 50, "Test", GRAY, BLACK)
        draw_button(10, screen_height - 60, 100, 50, "Exit", GRAY, BLACK)


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

    button_next = pygame.Rect(600, 500, 200, 50)
    button_done = pygame.Rect(600, 550, 200, 50)
    button_audio = pygame.Rect(600, 450, 200, 50)
    button_test = pygame.Rect(600, 400, 200, 50)
    button_exit = pygame.Rect(10, screen_height - 60, 100, 50)  # Adjust position and size as needed


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button_exit.collidepoint(mouse_pos):
                    print("Exit Button clicked!")
                    from Map.MainMap import main1
                    main1()  # Call the main function

                if button_next.collidepoint(mouse_pos):
                    print("Next Button clicked!")
                    numWordSeen += 1
                    recognized_text = ""  # Reset recognized text when moving to the next word

                elif button_done.collidepoint(mouse_pos):
                    print("Done Button clicked")
                    from Map.MainMap import main1
                    main1(2)
                elif button_audio.collidepoint(mouse_pos):
                    print("Play Audio Button clicked!")
                    play_audio(audio_files[numWordSeen % 5])

                if button_test.collidepoint(mouse_pos):
                    print("Test Button clicked!")
                    audio_input = capture_audio()
                    recognizer = sr.Recognizer()

                    try:
                        recognized_text = recognizer.recognize_google(audio_input, language='zh-CN')
                        if recognized_text == word_files[numWordSeen % 5]:
                            display_message("Correct")
                        else:
                            display_message("Incorrect")
                    except sr.UnknownValueError:
                        recognized_text = "Could not understand audio"
                    except sr.RequestError as e:
                        recognized_text = "Error: {0}".format(e)


        screen.fill(WHITE)

        # Draw buttons and show data
        display_data()

        pygame.display.flip()

    # Quit Pygame properly
    pygame.quit()
    sys.exit()

    
