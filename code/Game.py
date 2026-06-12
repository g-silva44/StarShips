import pygame as pg

from code.Const import WIN_HEIGHT, WIN_WIDTH, MENU_OPTION
from code.Level import Level
from code.Menu import Menu, MENU_OPTION

class Game:
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):

        while True:

            menu = Menu(self.window)
            menu_return = menu.run()


            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTION[4]:
                quit() # Exit the program
            else:
                pass

            # Check for all events
            for event in pg.event.get():
                # If the event is of type QUIT, then exit the program
                if event.type == pg.QUIT: # Close window
                    quit() # Exit the program

