from node import Node
from point import Point
class AStar:
    def __init__(self,rows,cols, head, apple, closed):
        self.closed = closed[:]
        self.open = [head]
        self.head = head
        self.apple = apple
        self.rows=rows
        self.cols=cols
        self.grid = [[Node(abs(apple.getx() - x) + abs(apple.gety() - y)) for y in range(cols)] for x in range(rows)]
        self.grid[head.getx()][head.gety()].setg(-1)
        self.parent={}

    def minFinOpen(self):
        min= float('inf')
        node = None
        for n in self.open:
            if self.grid[n.getx()][n.gety()].f() < min:
                min = self.grid[n.getx()][n.gety()].f()
                node=n
        return node or False
    
    def getmoves(self,p):
        moves = [
        (p.getx() - 1, p.gety()),  
        (p.getx() + 1, p.gety()), 
        (p.getx(), p.gety() - 1),  
        (p.getx(), p.gety() + 1)   
        ]
        valid_moves = [
        Point(x, y) for x, y in moves
        if 0 <= x < self.rows and 0 <= y < self.cols
        ]
        valid_moves = [m for m in valid_moves if m not in self.closed]
        return valid_moves

    def run(self):
        while True:
            current = self.minFinOpen()
            if not current :
                return 
            self.open.remove(current)
            self.closed.append(current)

           
            if current == self.apple:
                print(self.closed)
                return 
            moves = self.getmoves(current)
        
            if not moves : continue
         
            for move in  moves:
                if self.grid[move.getx()][move.gety()].newfshorter(self.grid[current.getx()][current.gety()].getg()) or not (move in self.open):
                    self.grid[move.getx()][move.gety()].setg(self.grid[current.getx()][current.gety()].getg())
                    self.parent[move] = current
                    if not (move in self.open):
                        self.open.insert(0,move)
            
        
                        

    def finalPath(self):
        path = []
        current = self.apple
        while current != self.head:
            path.append(current)
            current = self.parent.get(current)
            if current is None:  
                return []
        path.append(self.head)
        path.reverse()
        return path
    
    def printparent(self):
        print(self.parent)
    def print_grid(self):
        for row in self.grid:
            print(" | ".join(str(cell) for cell in row))
            print("-" * (len(row) * 12 - 1)) 

# test = AStar(10,10,Point(4,2),Point(0,6),[Point(4, 4), Point(3, 4), Point(2, 4), Point(1, 4), Point(1, 3), Point(1, 2), Point(2, 2), Point(3, 2)])
# test.run()
# print("finalPath")
# print(test.finalPath())
# test.printparent()

# print(test.closed)
# print(test.open)






            