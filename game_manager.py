import pygame


class GameManager:
    # singleton pattern
    _self = None

    def __new__(cls):
        if cls._self is None:
            cls._self = super().__new__(cls)
        return cls._self

    def __init__(self):
        self.game_active = False
        self.start_time = 0
        self.score = 0

    def get_score(self):
        self.score = int(pygame.time.get_ticks() / 1000) - self.start_time

    def start_game(self):
        self.game_active = True
        self.score = 0
        self.start_time = int(pygame.time.get_ticks() / 1000)
