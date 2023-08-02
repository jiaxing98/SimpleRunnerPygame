import pygame

from sys import exit
from audio_manager import AudioManager
from game_manager import GameManager
from ui_manager import UIManager

pygame.init()
clock = pygame.time.Clock()

# managers
am = AudioManager()
gm = GameManager()
um = UIManager()

# timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

am.bg_music.play(loops=-1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()  # safer way to close the program

        if gm.game_active:
            if event.type == obstacle_timer:
                um.spawn_enemy()
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                gm.start_game()

    if gm.game_active:
        gm.get_score()
        um.game_scene(gm.score)
        gm.game_active = not um.check_collision()
    else:
        um.main_menu(gm.score)

    pygame.display.update()
    clock.tick(60)  # fps no more than 60
