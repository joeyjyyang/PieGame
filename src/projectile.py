import pygame
import os
from hitbox import HitBox

class Projectile:
        shuriken = pygame.image.load(os.path.join('sprites', 'shuriken.png'))

        def __init__(self, x, y, direction):
                self.x = x
                self.y = y
                self.direction = direction
                self.vel = 8 * direction
                self.hitbox = HitBox(self.x, self.y, 40, 40).rectangle

        def animate(self, window):
                window.blit(self.shuriken, (self.x, self.y))
                self.hitbox = HitBox(self.x, self.y, 40, 40).rectangle
                pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2) #draw hitbox
            
