class Node:
    def __init__(self, h):
        self.h = h
        self.g = 1

    def f(self):
        return self.g + self.h
    def setg(self,g):
        self.g = g+1
    def getg(self):
        return self.g
    def newfshorter(self,g):
        return (self.h + g) < self.f()
    def __repr__(self):
        return f"Cell(h: {self.h}, g: {self.g})"
