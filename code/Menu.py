import sys

import pygame as pg

from code.Const import COLOR_ORANGE, MENU_OPTION
from code.Const import COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pg.image.load("asset/bg.png").convert()
        self.rect = self.window.get_rect()
        self.clock = pg.time.Clock()

    def run(self):
        menu_option = 0
        # Initialize mixer if needed and safely start music
        try:
            if not pg.mixer.get_init():
                pg.mixer.init()
        except Exception:
            pass

        try:
            pg.mixer.music.load("asset/fase1.mp3")
            pg.mixer.music.play(-1)  # Loop the music
            pg.mixer.music.set_volume(0.1)
        except Exception:
            pass

        running = True
        while running:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    try:
                        pg.mixer.music.stop()
                    except Exception:
                        pass
                    pg.quit()
                    sys.exit()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0

                    if event.key == pg.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1

                    if event.key == pg.K_RETURN: #ENTER
                        return MENU_OPTION[menu_option]


            # Draw background first, then text
            bg = pg.transform.scale(self.surf, self.window.get_size())
            self.window.blit(bg, (0, 0))
            self.menu_text("Mountain", 48, COLOR_ORANGE, (self.rect.centerx, self.rect.centery - 120))
            self.menu_text("Shooter", 48, COLOR_ORANGE, (self.rect.centerx, self.rect.centery - 70))
            
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(MENU_OPTION[i], 20, COLOR_ORANGE, (self.rect.centerx, self.rect.centery + i * 25))
                else:
                    self.menu_text(MENU_OPTION[i], 20, COLOR_WHITE, (self.rect.centerx, self.rect.centery + i * 25))

            pg.display.flip()
            self.clock.tick(60)  # Limit to 60 FPS

        try:
            pg.mixer.music.stop()
        except Exception:
            pass
        return

    def menu_text(self, text, size, color, pos):
        font = pg.font.SysFont("Arial", size, bold=True)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=pos)
        self.window.blit(text_surface, text_rect)