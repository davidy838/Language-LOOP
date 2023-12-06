import pygame
import Map.settings as settings
import Components.vocabPractice as vp
from Components.testMenu import test_menu
from Components.speech import doSpeechPractice
from Components.player import Player
from Map.tilemanager import TileManager
from pygame import mixer
from Map.MainMap import main1



def start_menu(screen):
    screen.fill((0, 128, 0))  
    font = pygame.font.Font(None, 36)
    font1 = pygame.font.Font(None, 26)
    start_text = font1.render("Press 'S' to start", True, (255, 255, 255))
    title_text_line1 = font.render("Language LOOP", True, (255, 255, 255))
    title_text_line2 = font.render("Interactive Game By David Yang", True, (255, 255, 255))
    title_text_line3 = font.render("Vancouver, Canada", True, (255, 255, 255))
    screen.blit(title_text_line1, (200, 200))
    screen.blit(title_text_line2, (200, 250))
    screen.blit(title_text_line3, (200, 300))
    screen.blit(start_text, (200, 350))
    pygame.display.update()


def main(gamestate):
    pygame.init()
    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    mixer.init() 
    

    mixer.music.load("/Users/davidyang/Desktop/Language LOOP/audio/song 2.mp3") 
    

    mixer.music.set_volume(0.1) 
    

    mixer.music.play(-1) 

    tile_manager = TileManager(settings.MAP_DATA)
    player = None
    show_start_menu = True  
    while show_start_menu:
        start_menu(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    show_start_menu = False  

        pygame.display.update()
    main1(gamestate)
if __name__ == "__main__":
    main(1)