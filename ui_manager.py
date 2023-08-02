import constant
import pygame

from obstacle import Obstacle
from player import Player
from random import choice


class UIManager:
    # singleton pattern
    _self = None

    def __new__(cls):
        if cls._self is None:
            cls._self = super().__new__(cls)
        return cls._self

    def __init__(self):
        # window
        caption = constant.GAME_NAME
        self.screen = pygame.display.set_mode(
            (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
        pygame.display.set_caption(caption)

        # surfaces
        self.sky_surface = pygame.image.load(
            "artworks/backgrounds/sky.png").convert()
        self.ground_surface = pygame.image.load(
            "artworks/backgrounds/ground.png").convert()
        self.player_surface = pygame.image.load(
            "artworks/player/player_stand.png").convert_alpha()

        # font
        font_type = "fonts/Pixeltype.ttf"
        font_size = 50
        self.font = pygame.font.Font(font_type, font_size)

        # groups
        self.player = pygame.sprite.GroupSingle()
        self.obstacle_group = pygame.sprite.Group()
        self.player.add(Player())

        self.main_menu()

    def main_menu(self, score=0):
        player_surface = pygame.transform.rotozoom(
            self.player_surface, 0, 2)
        player_rect = player_surface.get_rect(
            center=(400, 200))

        game_name = self.font.render(
            constant.GAME_NAME, False, (111, 196, 169))
        game_name_rect = game_name.get_rect(center=(400, 80))

        game_message = self.font.render(
            "Press space to run", False, (111, 196, 169))
        game_message_rect = game_message.get_rect(center=(400, 320))

        score_message = self.font.render(
            f"Your score: {score}", False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center=(400, 330))

        # start painting
        self.screen.fill((94, 129, 162))
        self.screen.blit(game_name, game_name_rect)
        self.screen.blit(player_surface, player_rect)

        if score == 0:
            self.screen.blit(game_message, game_message_rect)
        else:
            self.screen.blit(score_message, score_message_rect)

    def game_scene(self, score):
        rgb = (64, 64, 64)
        score_surface = self.font.render(f"Score: {score}", False, rgb)
        score_rect = score_surface.get_rect(center=(400, 50))

        self.screen.blit(self.sky_surface, (0, 0))
        self.screen.blit(self.ground_surface, (0, 300))
        self.screen.blit(score_surface, score_rect)

        self.player.draw(self.screen)
        self.player.update()

        self.obstacle_group.draw(self.screen)
        self.obstacle_group.update()

    def spawn_enemy(self):
        self.obstacle_group.add(
            Obstacle(choice([constant.FLY, constant.SNAIL, constant.SNAIL, constant.SNAIL])))

    def check_collision(self):
        if pygame.sprite.spritecollide(self.player.sprite, self.obstacle_group, False):
            self.obstacle_group.empty()
            return True
        else:
            return False
