import tkinter as tk
import time
import random
from point import Point
from a_star import AStar
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("serpent AI")
        self.root.geometry("700x600")
        self.grid_frame = None

        # First Page
        self.start_page()

    def start_page(self):
        self.clear_frame()

        start_button = tk.Button(
            self.root,
            text="Start Game",
            command=self.main_page,
            font=("Arial", 16, "bold"),      
            bg="#74BF6B",                
            activebackground="#EDEBE2",     
            fg="white",                     
            borderwidth=2,                  
            relief="ridge",                  
            highlightthickness=0            
        )
        start_button.pack(
            expand=True,
            padx=20,    
            pady=20     
        )

    def main_page(self):
        # Clear the first page
        self.clear_frame()

        rows, cols = 10, 10  
        self.grid_frame = tk.Frame(self.root)
        self.grid_frame.pack(expand=True)

        self.cells = {}
        for i in range(rows):
            for j in range(cols):
                cell = tk.Label(self.grid_frame, width=6, height=3, borderwidth=1, relief="flat", bg="#EDEBE2",highlightbackground="white", highlightthickness=1)
                cell.grid(row=i, column=j)
                self.cells[(i, j)] = cell

        obst=[Point(1,7),Point(1,8),Point(2,8),Point(7,1), Point(8,1),Point(8,2),Point(4,4),Point(5,5)]
        self.color_cell(3,3,"#74BF6B")
        self.color_cell(3,2,"#19a337")
        self.color_cell(3,1,"#19a337")
        self.color_cells(obst,"brown")
        self.color_cell(0,1,"red")

        self.root.after(1000, lambda: self.start_game())

    def start_game(self):
        def game_loop():
            nonlocal head, apple, closed

            astar = AStar(10, 10, head, apple, closed+obst)
            astar.run()
            path = astar.finalPath() 
            if path:
                path.pop(0)  
                path.pop() 
            else:
                return  
            
            closed.append(head)
            def traverse_path(index=0):
                if index < len(path):
                    self.color_cell(closed[0].getx(), closed[0].gety(), "#EDEBE2")
                    for i in range(len(closed) - 1):
                        closed[i] = closed[i + 1]
                        self.color_cell(closed[i].getx(), closed[i].gety(), "#19a337")

                    closed[-1] = path[index]
                    self.color_cell(closed[-1].getx(), closed[-1].gety(), "#74BF6B")

                    self.root.after(100, lambda: traverse_path(index + 1))
                else:
                    self.color_cell(apple.getx(), apple.gety(), "#74BF6B")
                    self.color_cell(closed[-1].getx(), closed[-1].gety(), "#19a337")
                    continue_game()
            traverse_path()

        def continue_game():
            nonlocal head, apple, closed
            head = apple
            apple = self.random_apple(10, 10, closed + [head]+obst)
            if not apple:
                return  

            self.color_cell(apple.getx(), apple.gety(), "red")
            self.root.after(200, game_loop)

        # Initial setup
        head = Point(3, 3)
        apple = Point(0, 1)
        closed = [Point(3, 1),Point(3, 2)]
        obst=[Point(1,7),Point(1,8),Point(2,8),Point(7,1), Point(8,1),Point(8,2),Point(4,4),Point(5,5)]
        


        # Start the game loop
        game_loop()

        
    def color_cell(self, x, y, color):
        cell = self.cells.get((x, y))
        if cell:
            cell.config(bg=color)  
            if color=="#EDEBE2":cell.config(highlightbackground="white")
            else: cell.config(highlightbackground="#0f4d0f")

    def color_cells(self, cells, color):
        for c in cells:
            cell = self.cells.get((c.getx(), c.gety()))
            cell.config(bg=color) 
            cell.config(highlightbackground="black")

    def random_apple(self, rows, cols, closed):
        excluded_set = set((p.getx(), p.gety()) for p in closed)
        all_points = {(x, y) for x in range(rows) for y in range(cols)}
        available_points = all_points - excluded_set
        if not available_points:
            return None
        random_point = random.choice(list(available_points))
        return Point(random_point[0], random_point[1])

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Create the application
root = tk.Tk()
app = App(root)
root.mainloop()
