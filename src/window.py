import pygame
import os

class Window:
        bg = pygame.image.load(os.path.join('sprites', 'bg.jpg'))
        
        def __init__(self, windowHeight, windowWidth, player, enemies):
                self.windowHeight = windowHeight
                self.windowWidth = windowWidth
                self.window = pygame.display.set_mode((self.windowHeight, self.windowWidth))
                self.player = player
                self.enemies = enemies
                pygame.display.set_caption("Spaghetti User Interface")

        def updateWindow(self):
                self.window.blit(self.bg, (0,0)) 
                self.player.animate(self.window)
                for enemy in self.enemies:
                        enemy.animate(self.window)
                for projectile in self.player.projectiles:
                        projectile.animate(self.window)
                pygame.display.update()
