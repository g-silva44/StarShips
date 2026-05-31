import pygame as pg

from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.Menu import Menu

class Game:
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):

        while True:

            menu = Menu(self.window)
            menu.run()
            pass

            # Check for all events
            for event in pg.event.get():
                # If the event is of type QUIT, then exit the program
                if event.type == pg.QUIT: # Close window
                    quit() # Exit the program

