from code.Const import ENTITY_SPEED
from code.Entity import Entity

class Background(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)

    def move(self):
        self.rect.x -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.x += self.rect.width * 2