import pygame
import os

import Components.player as player
import Map.settings as settings
import Map.tile as tile

class TileManager:
    def __init__(self, map_data):
        self.map_tile_num = map_data
        self.tiles = [None] * 50  # Adjust based on the number of tile types
        self.load_tile_images()

    def load_tile_images(self):
        self.setup(0, 'tiles/CherryTree01.png', True)
        self.setup(1, 'tiles/Tree01.png', True)
        self.setup(2, 'tiles/Grass01.png', False)
        self.setup(3, 'tiles/grass02.png', False)
        self.setup(4, 'tiles/Water01.png', True)
        self.setup(5, 'tiles/Water02.png', True)
        self.setup(6, 'tiles/Door01.png', True)



    def setup(self, index, image_name, collision):  # Method to setup each tile
        try:
            image = settings.resize_tile(os.path.join(image_name))
            self.tiles[index] = tile.Tile(image, collision)
        except Exception as e:
            print(f"Error loading image {image_name}: {e}")

    def draw(self, screen, player):
        for row_idx, row in enumerate(self.map_tile_num):
            for col_idx, tile_num in enumerate(row):
                tile = self.tiles[tile_num]
                if tile:
                    # Calculate the world position of the tile
                    world_x = col_idx * settings.TILE_SIZE
                    world_y = row_idx * settings.TILE_SIZE

                    # Calculate the position on the screen
                    screen_x = world_x - player.rect.x + settings.PLAYER_SCREEN_X
                    screen_y = world_y - player.rect.y + settings.PLAYER_SCREEN_Y

                    # Check if the tile is within the player's viewport
                    if (world_x + settings.TILE_SIZE > player.rect.x - settings.PLAYER_SCREEN_X and
                            world_x - settings.TILE_SIZE < player.rect.x + settings.PLAYER_SCREEN_X and
                            world_y + settings.TILE_SIZE > player.rect.y - settings.PLAYER_SCREEN_Y and
                            world_y - settings.TILE_SIZE < player.rect.y + settings.PLAYER_SCREEN_Y):
                        # Draw the tile
                        screen.blit(tile.image, (screen_x, screen_y))

