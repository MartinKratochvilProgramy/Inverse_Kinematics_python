import math

class Section:
    #point A is the starting point and B is the ending point of section
    def __init__(self, xa, ya, L, phi, width):
        self.xa = xa
        self.ya = ya
        self.L = L
        self.phi = phi
        self.width = width

    def update(self):
        self.xb = self.xa + self.L * math.cos(self.phi)
        self.yb = self.ya + self.L * math.sin(self.phi)