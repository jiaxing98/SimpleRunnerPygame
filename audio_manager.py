import pygame


class AudioManager:
    # singleton pattern
    _self = None

    def __new__(cls):
        if cls._self is None:
            cls._self = super().__new__(cls)
        return cls._self

    def __init__(self):
        self.jump_sound = pygame.mixer.Sound("audio/jump.mp3")
        self.bg_music = pygame.mixer.Sound("audio/music.wav")

    def jump(self, volume=0.5):
        self.jump_sound.set_volume(volume)
        self.jump_sound.play()
