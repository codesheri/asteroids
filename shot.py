import pygame
from circleshape import CircleShape
from constants import PLAYER_SHOOT_SPEED


class Shot(CircleShape):
    def __init__(self, x, y, radius, rotation):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 1).rotate(rotation) * PLAYER_SHOOT_SPEED

    def draw(self, screen):
        pygame.draw.circle(
            screen, "white", (int(self.position.x), int(self.position.y)), self.radius
        )

    def update(self, dt):
        self.position += self.velocity * dt
