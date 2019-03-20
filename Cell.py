class Cell:
    
    def __init__(self, x, y, i, level, wid):
        self.x = x
        self.y = y
        self.r, self.g, self.b = 93, 81, 252
        self.measure = wid/level
        self.index = i
        self.is_mine = False
        self.visited = False
        self.neighbors = []
        self.mine_neighbors = 0
        self.level = level
        self.wid = wid
        
    def show(self, r, g, b):
        fill(r, g, b)
        rect(self.x, self.y, self.x + self.measure, self.y + self.measure)
   
    #--- drawing mine ---#
    
    def draw_mine(self):
        if self.is_mine:
            fill(16)
            if self.visited:
                ellipse(self.x + abs(self.measure/2), self.y + abs(self.measure/2), abs(self.measure/2), abs(self.measure/2))
   
    #--- getting all neighbors of a cell (ugly but worth) ---#     
           
    def neighbor(self, arr_cells):
        lin = abs(self.index / self.level)
        col = self.index % self.level
        if lin == 0:
            if col == 0:
                for i in range(2):
                    for j in range(2):
                        if i or j:
                            self.neighbors.append(arr_cells[lin + i][col + j])

            elif col == (self.level - 1):
                for i in range(2):
                    for j in range(2):
                        if i or j:
                            self.neighbors.append(arr_cells[lin + i][col - j])
            else:
                for i in range(2):
                    for j in range(-1,2):
                        if i or j:
                            self.neighbors.append(arr_cells[lin + i][col + j])
                                
        elif lin == (self.level - 1):
            if col == 0:
                for i in range(2):
                    for j in range(2):
                        if i or j:
                            self.neighbors.append(arr_cells[lin - i][col + j])
            elif col == (self.level - 1):
                for i in range(2):
                    for j in range(2):
                        if i or j:
                            self.neighbors.append(arr_cells[lin - i][col - j])
            else:
                for i in range(2):
                    for j in range(-1,2):
                        if i or j:
                            self.neighbors.append(arr_cells[lin - i][col + j])
                            
        elif col == 0:
            for i in range(-1,2):
                for j in range(2):
                    if i or j:
                        self.neighbors.append(arr_cells[lin + i][col + j])
                        
        elif col == (self.level - 1):
            for i in range(-1,2):
                for j in range(2):
                    if i or j:
                        self.neighbors.append(arr_cells[lin + i][col - j])
                                
        else:
            for i in range(-1,2):
                for j in range(-1,2):
                    if i or j:
                        self.neighbors.append(arr_cells[lin + i][col + j])
                        
    #--- counting all the neighbors that have mines ---#
    
    def mine_neighbor(self):
        for i in self.neighbors:
            if i.is_mine:
                self.mine_neighbors += 1
                         
    #--- drawing number of neighbors that have mines ---#
    
    def number(self):
        if not self.is_mine:
            textSize(18)
            if self.visited:
                if self.mine_neighbors:
                    if self.mine_neighbors == 1:
                        fill(0, 41, 214)
                    elif self.mine_neighbors == 2:
                        fill(0, 153, 51)
                    elif self.mine_neighbors == 3:
                        fill(224, 0, 0)
                    elif self.mine_neighbors == 4:
                        fill(77, 0, 153)
                    elif self.mine_neighbors == 5:
                        fill(128, 0, 0)
                    elif self.mine_neighbors == 6:
                        fill(0, 153, 153)
                    elif self.mine_neighbors == 7:
                        fill(0)
                    elif self.mine_neighbors == 8:
                        fill(100)
                    text(str(self.mine_neighbors), self.x + abs(self.measure/2) - 5, self.y + abs(self.measure/2) + 8)
