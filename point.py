class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def getx(self):
        return self.x
    def gety(self):
        return self.y
    def setp(self,x,y):
        self.x=x
        self.y=y

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
            