import time

class buff:
    def __init__(self, character):
        self.char = character
        self.origiHealth = character.health
        self.origiGravity = character.gravity

    def health_buff(self): # infinite health
        self.char.health = 100000

    def long_jump(self):
        self.char.gravity = 0.1

    def clear(self): # clear everything when died
        self.char.health = self.origiHealth
        self.char.gravity = self.origiGravity