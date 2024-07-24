# import pgzrun
from pgzero.actor import Actor

class CustomActor(Actor):
    def __init__(self, image='spaceship', pos=(256, 460), **kwargs):
        super().__init__(image, pos)
        # Initialize additional variables
        # self.health = kwargs.get('health', 100)
        # self.speed = kwargs.get('speed', 5)
        # self.score = kwargs.get('score', 0)    
    def logic(self, keyboard, SPEED):
        if keyboard.left:
            self.x -= SPEED
            if (self.x < 0): self.x = 0
        elif keyboard.right:
            self.x += SPEED
            if (self.x > 512): self.x = 512




