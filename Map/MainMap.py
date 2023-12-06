import pygame
import Map.settings as settings
import sys
sys.path.append("Components")
import Components.vocabPractice as vp
from Components.testMenu import test_menu
from Components.speech import doSpeechPractice
from Components.player import Player
from Map.tilemanager import TileManager
from pygame import mixer



def main1(gamestate):
    pygame.init()
    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    mixer.init() 
    

    mixer.music.load("/Users/davidyang/Desktop/Language LOOP/audio/song 2.mp3") 
    

    mixer.music.set_volume(0.3) 
    

    mixer.music.play(-1) 

    tile_manager = TileManager(settings.MAP_DATA)
    player = None


    if gamestate == 0:
        player = Player(380, 250, tile_manager)

    if gamestate == 1:
        player = Player(380, 520, tile_manager)

    if gamestate == 2:
        player = Player(380, 840, tile_manager)

    if gamestate == 3:
        player = Player(380, 840, tile_manager)


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.update(keys)

        screen.fill((0, 0, 0))  # Clear screen
        tile_manager.draw(screen, player)
        player.draw(screen)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main1(1)

def hit_door_1():
    vp.doVocabPractice('module1')

def hit_door_2():
    doSpeechPractice('module1')

def hit_door_3():
    test_menu()
#   mixer.init() 
    

#    mixer.music.load("song.mp3") 
    

#    mixer.music.set_volume(0.7) 
    

 #   mixer.music.play(-1) 