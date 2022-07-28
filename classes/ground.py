from assets import GROUND_IMAGE


# Ground object
class Ground:
    VELOCITY = 5
    WIDTH = GROUND_IMAGE.get_width()
    IMAGE = GROUND_IMAGE

    def __init__(self, y):
        self.y = y
        self.x0 = 0
        self.x1 = self.WIDTH

    def move(self):
        self.x0 -= self.VELOCITY
        self.x1 -= self.VELOCITY

        if self.x0 + self.WIDTH < 0:
            self.x0 = self.x1 + self.WIDTH
        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x0 + self.WIDTH

    def draw(self, screen):
        screen.blit(self.IMAGE, (self.x0, self.y))
        screen.blit(self.IMAGE, (self.x1, self.y))
