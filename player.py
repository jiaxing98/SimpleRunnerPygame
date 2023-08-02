import pygame

from audio_manager import AudioManager


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # audio manager
        self.am = AudioManager()

        # walk
        player_walk_1 = pygame.image.load(
            "artworks/player/player_walk_1.png").convert_alpha()
        player_walk_2 = pygame.image.load(
            "artworks/player/player_walk_2.png").convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]

        # jump
        self.player_jump = pygame.image.load(
            "artworks/player/player_jump.png").convert_alpha()

        self.player_index = 0
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(200, 300))
        self.gravity = 0

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.am.jump()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]
