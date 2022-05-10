import pygame


class Sound():
    def __init__(self):
        self.new_level = pygame.mixer.Sound("music\level_up.ogg")
        self.fail = pygame.mixer.Sound("music\gg_lox.ogg")
        self.crash_sound = pygame.mixer.Sound("music\crash.ogg")
        self.pip_sound = pygame.mixer.Sound("music\pip.ogg")
        self.play_button = pygame.mixer.Sound("music\play_button.ogg")
        self.damage = pygame.mixer.Sound("music\hurt.ogg")
