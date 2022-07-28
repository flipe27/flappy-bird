import pygame
import os

# Game images
GAME_ICON = pygame.image.load(os.path.join('imgs', 'icon.png'))
GAME_LOGO = pygame.image.load(os.path.join('imgs', 'logo.png'))
RESTART_IMAGE = pygame.image.load(os.path.join('imgs', 'restart_button.png'))
PIPE_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))
GROUND_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
BACKGROUND_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))
BIRD_IMAGES = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png')))
]

# Game fonts
pygame.font.init()
POINTS_FONT = pygame.font.SysFont('arial', 40)
START_FONT = pygame.font.SysFont('arial', 20)

# Game sounds
pygame.mixer.init()
pygame.mixer.music.load(os.path.join('songs', 'ost.mp3'))

PASSED = pygame.mixer.Sound(os.path.join('songs', 'passed.mp3'))
PASSED.set_volume(0.1)
