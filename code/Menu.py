import pygame


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("asset/bg.png")
        self.rect = self.window.get_rect()

    def run(self):
        bg = pygame.transform.scale(self.surf, self.window.get_size())
        self.window.blit(bg, self.rect)
        pygame.display.flip()