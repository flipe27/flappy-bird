from assets import PIPE_IMAGE, pygame
import random


# Pipe object
class Pipe:
    DISTANCE = 200
    VELOCITY = 5

    def __init__(self, x):
        self.x = x
        self.height = 0
        self.top_pos = 0
        self.base_pos = 0
        self.TOP_PIPE = pygame.transform.flip(PIPE_IMAGE, False, True)
        self.BASE_PIPE = PIPE_IMAGE
        self.passed = False
        self.set_height()

    def set_height(self):
        self.height = random.randrange(50, 250)
        self.top_pos = self.height - self.TOP_PIPE.get_height()
        self.base_pos = self.height + self.DISTANCE

    def move(self):
        self.x -= self.VELOCITY

    def draw(self, screen):
        screen.blit(self.TOP_PIPE, (self.x, self.top_pos))
        screen.blit(self.BASE_PIPE, (self.x, self.base_pos))

    # Bird colliding with the pipes
    def collide(self, bird):
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.TOP_PIPE)
        base_mask = pygame.mask.from_surface(self.BASE_PIPE)

        top_distance = (self.x - bird.x, self.top_pos - round(bird.y))
        base_distance = (self.x - bird.x, self.base_pos - round(bird.y))

        top_point = bird_mask.overlap(top_mask, top_distance)
        base_point = bird_mask.overlap(base_mask, base_distance)

        if top_point or base_point:
            return True
        else:
            return False
