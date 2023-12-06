import pygame

import Map.MainMap as MainMap
import Map.settings as settings
import Map.tilemanager as tilemanager


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, tilemanager):
        super().__init__()
        self.tile_manager = tilemanager
        self.solid_area = pygame.Rect(settings.TILE_SIZE / 4, settings.TILE_SIZE / 4, settings.TILE_SIZE / 2, settings.TILE_SIZE / 2)
        self.collision_on = False
        self.load_player_images()
        self.direction = 'down'
        self.current_frame = 1
        self.image = self.images[self.direction + str(self.current_frame)]
        self.rect = self.image.get_rect(topleft=(x,y))
        self.speed = 5
        self.animation_speed = 10
        self.animation_counter = 0

    def load_player_images(self):
        self.images = {
            'up1': settings.resize_tile('sprites/PandaUp01.png'),
            'up2': settings.resize_tile('sprites/PandaUp02.png'),
            'down1': settings.resize_tile('sprites/PandaUp01.png'),
            'down2': settings.resize_tile('sprites/PandaUp02.png'),
            'left1': settings.resize_tile('sprites/PandaLeft01.png'),
            'left2': settings.resize_tile('sprites/PandaLeft02.png'),
            'right1': settings.resize_tile('sprites/PandaRight01.png'),
            'right2': settings.resize_tile('sprites/PandaRight02.png')
        }

    def update(self, keys):
        moving = False

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction = 'left'
            moving = True
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction = 'right'
            moving = True
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction = 'up'
            moving = True
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction = 'down'
            moving = True

        if moving:
            if not self.collision_on:
                self.rect.x += self.speed if self.direction == 'right' else -self.speed if self.direction == 'left' else 0
                self.rect.y += self.speed if self.direction == 'down' else -self.speed if self.direction == 'up' else 0
            self.animate()
        else:                self.current_frame = 1  # Reset to the first frame when not moving

        self.check_tile_collision()

        self.image = self.images[self.direction + str(self.current_frame)]

    def animate(self):
        self.animation_counter += 1


        if self.animation_counter >= self.animation_speed:
            self.animation_counter = 0
            self.current_frame = 2 if self.current_frame == 1 else 1

    def draw(self, screen):
        screen.blit(self.image, (settings.PLAYER_SCREEN_X, settings.PLAYER_SCREEN_Y))

    def check_tile_collision(self):
        # Calculate the entity's corners in the world
        left_world_x = self.rect.x + self.solid_area.x
        right_world_x = self.rect.x + self.solid_area.x + settings.TILE_SIZE
        top_world_y = self.rect.y + self.solid_area.y
        bottom_world_y = self.rect.y + self.solid_area.y + settings.TILE_SIZE

        # Convert these positions to tile coordinates
        left_col = left_world_x // settings.TILE_SIZE
        right_col = right_world_x // settings.TILE_SIZE
        top_row = top_world_y // settings.TILE_SIZE
        bottom_row = bottom_world_y // settings.TILE_SIZE
        print(bottom_row + 100)
        print(right_col)
        tile_num1 = settings.MAP_DATA[15][15]
        tile_num2 = settings.MAP_DATA[15][15]

        # Check collision based on direction
        # if self.direction == 'up':
        #     top_row = (top_world_y - self.speed) // settings.TILE_SIZE
        #     tile_num1 = settings.MAP_DATA[left_col][top_row]
        #     tile_num2 = settings.MAP_DATA[right_col][top_row]
        # elif self.direction == 'down':
        #     bottom_row = (bottom_world_y + self.speed) // settings.TILE_SIZE
        #     tile_num1 = settings.MAP_DATA[left_col][bottom_row]
        #     tile_num2 = settings.MAP_DATA[right_col][bottom_row]
        # elif self.direction == 'left':
        #     left_col = (left_world_x - self.speed) // settings.TILE_SIZE
        #     tile_num1 = settings.MAP_DATA[left_col][top_row]
        #     tile_num2 = settings.MAP_DATA[left_col][bottom_row]
        # elif self.direction == 'right':
        #     right_col = (right_world_x + self.speed) // settings.TILE_SIZE
        #     tile_num1 = settings.MAP_DATA[right_col][top_row]
        #     tile_num2 = settings.MAP_DATA[right_col][bottom_row]

        # Check if these tiles are collidable
        # if self.tile_manager.tiles[tile_num1].collision or self.tile_manager.tiles[tile_num2].collision or self.rect.x + self.speed > 1800 or self.rect.y + self.speed > 950:
        if self.rect.x > 560:
            self.collision_on = True
            self.rect.x = 560
        elif self.rect.x < 200:
            self.collision_on = True
            self.rect.x = 200
        elif self.rect.y > 360 and self.rect.y < 370:
            MainMap.hit_door_1()
        elif self.rect.y == 600:
            MainMap.hit_door_2()
        elif self.rect.y > 760 and self.rect.y < 770:
            MainMap.hit_door_3()
        elif self.rect.y < 200:
            self.collision_on = True
            self.rect.y = 200
        elif self.rect.y > 1000:
            self.collision_on = True
            self.rect.y = 1000
        else:
            self.collision_on = False


