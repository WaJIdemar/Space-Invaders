import pygame
from pygame.sprite import Group

from Sound import Sound
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard
from Settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Game")
    play_button = Button(ai_settings, screen, "Play")
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)

    background = pygame.image.load("images/back.bmp").convert()
    background = pygame.transform.scale(background,
                (ai_settings.screen_width, ai_settings.screen_height))                         

    sound = Sound()

    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets,
                        sound)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets, sound)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets, sound)

        gf.update_screen(background, screen, stats, sb, ship, aliens, bullets,
                         play_button)
        

run_game()
