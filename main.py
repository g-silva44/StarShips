try:
    import pygame as pg
except Exception:
    # Fallback stub so linters/IDEs don't report unresolved import and
    # so the rest of the file can be inspected or run without pygame.
    import types
    pg = types.SimpleNamespace()
    pg.init = lambda: None
    pg.display = types.SimpleNamespace(set_mode=lambda *args, **kwargs: None)


pg.init()
screen = pg.display.set_mode(size=(600, 480))
while True:
    # Check for all events
    for event in pg.event.get():
        # If the event is of type QUIT, then exit the program
        if event.type == pg.QUIT: # Close window
            quit() # Exit the program