import pygame as pg

from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.Menu import Menu

class Game:
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):

        pg.mixer_music.load("asset/fase1.mp3")
        pg.mixer_music.play(-1)  # Loop the music
        pg.mixer_music.set_volume(0.1)  # Set the volume (0.0 to 1.0)

        while True:

            menu = Menu(self.window)
            menu.run()
            pass

            # Check for all events
            for event in pg.event.get():
                # If the event is of type QUIT, then exit the program
                if event.type == pg.QUIT: # Close window
                    quit() # Exit the program

