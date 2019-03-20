'''      - MINESWEEPER -

Reproducing a famous computer game
using Python on Processing.     

Matheus de Moncada Assis       '''

import Cell as c
import time as t

'''       SET DIFFICULTY

 1 -> begginers
 2 -> intermediate
 3 -> expert                   '''

diff = 3

if diff == 1:
    level = 8
    n_mines = 10
    wid, hei = 280, 280
elif diff == 2:
    level = 16
    n_mines = 40
    wid, hei = 560, 560
elif diff == 3:
    level = 24
    n_mines = 99
    wid, hei = 840, 840


mines = []
pos_cells = [i for i in range(level**2)]

#--- selecting cells that are mines ---#

for i in range(n_mines):
    index = int(random(len(pos_cells)))
    mines.append(pos_cells[index])
    pos_cells.remove(pos_cells[index])

#--- creating all the cells and defining the mines ---#
    
cells = [[c.Cell(abs((wid/level)*i), abs((hei/level)*j), level*j + i, level, wid) for i in range(level)] for j in range(level)]

for lines in cells:
    for cell in lines:
        if cell.index in mines:
                cell.is_mine = True
                
                #puxadinho incoming
                mines.remove(cell.index)
                mines.append(cell)

for lines in cells:
    for cell in lines:
        cell.neighbor(cells)
        cell.mine_neighbor()

t0 = t.time()

def setup():
    size(wid,hei)
    
def draw():
    global mines, cells, start_game, level, wid, t0
    
    for i in range(1,level):
        stroke(255)
        line((height/level)*i, 0, (height/level)*i, height)
        line(0, (width/level)*i, width, (width/level)*i)

    for lines in cells:
        for cell in lines:
            cell.show(cell.r, cell.g, cell.b)
                
            #--- opening the cell with a click ---#
                
            if mousePressed and (mouseX >= cell.x and mouseX <= cell.x + cell.measure) and (mouseY >= cell.y and mouseY <= cell.y + cell.measure):
                cell.visited = True
                cell.r, cell.g, cell.b = 192, 192, 192
                cell.show(cell.r, cell.g, cell.b)
                
                #--- losing the game if you click in a cell containing a mine ---#
                
                if cell.is_mine:
                    cell.r, cell.g, cell.b = 255, 0, 0
                    cell.show(cell.r, cell.g, cell.b)
                
                    #--- trying to show all mines on the field after losing (obviously it's not working) ---#
                    
                    #for mine in mines:
                    #    mine.visited = True
                    #    mine.r, mine.g, mine.b = 192, 192, 192
                    #    print(mine.r, mine.g, mine.b, mine)
                    #    mine.draw_mine()
                                
                    print('YOU LOST')
                    print('TIME: {}s'.format(int(t.time() - t0)))
                    noLoop()
                    
                #--- if you click in a blank cell, opening all neighbors ---#
                    
                if not cell.mine_neighbors and not cell.is_mine:
                    blank_cells = cell.neighbors
                    while len(blank_cells) > 0:
                        i = blank_cells[0]
                        i.visited = True
                        i.r, i.g, i.b = 192, 192, 192
                        i.show(cell.r, cell.g, cell.b)
                        if not i.mine_neighbors:
                            for neigh in i.neighbors:
                                if not neigh.visited:
                                    blank_cells.append(neigh)
                        blank_cells.remove(i)
                
        #--- drawing mines and numbers on all open cells ---#
                
            if cell.is_mine:
                cell.draw_mine()
        
            cell.number()
            
    #--- test if you won the game ---#
    if win(cells, level):
        print('YOU WON')
        print('TIME: {}s'.format(int(t.time() - t0)))
        noLoop()
      
        
def win(arr_cells, level):
    count = 0
    for lines in arr_cells:
        for cell in lines:
            if cell.is_mine:
                if not cell.visited:
                    count += 1
            else:
                if cell.visited:
                    count += 1
    if count == level**2:
        return True
    else:
        return False
