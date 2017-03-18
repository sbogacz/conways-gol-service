import numpy

glider_mask = [[1,1,1],[1,0,0],[0,1,0]]
herschel_mask = [[1,0,0],[1,1,1],[1,0,1],[0,0,1]]

class Grid:
  """ A class to encapsulate Conway's Game of Life """
  def __init__(self, w, h):
    self.width = w
    self.height = h
    g = [numpy.zeros(self.width) for i in range(self.height)]
    self.grid = g

  def Print(self):
    """ Print simply prints the current state of the grid to stdout. \ 
        Note that there is no locking, therefore Step and Print should \
        only be called sequentially """
    out = ""
    for i in range(self.height):
      for j in range(self.width):
        out += "." if (self.grid[i][j]) == 0 else "@"
      out += "\n"
    print(out)

  def Glider(self, x, y):
    """ sets glider with top right corner at i,j """
    self.apply_mask(x,y,glider_mask)

  def Herschel(self, x, y):
    """ sets a mask of the Hershcel glider with the top right corner at i,j """
    self.apply_mask(x,y,herschel_mask)

  def apply_mask(self, x, y, mask):
    """ a method intended for internal class use only """
    for i in range(len(mask)):
      for j in range(len(mask[0])):
        m = i+(x%self.height)
        n = j+(y%self.width)
        self[m][n] = mask[i][j]   

  def __getitem__(self, item):
    """ getitem to allow self to be indexed directly """
    return self.grid[item]

  def score(self, x, y):
    """ given x and y coordinates, it returns the number of live neighbors \
        and a bool to indicate if self[x][y] is alive. Intended for internal \
        use only """
    scr=0
    isAlive=False
    for i in range(x-1,x+2):
      m = i % self.height
      for j in range(y-1,y+2):
        n = j % self.width
        if i == x and j == y:
          isAlive=self[m][n]==1
          continue
        scr += self[m][n]
    return scr, isAlive

  def Step(self):
    """ Step updates the grid according to Conway's Game of Life Rules. \
        1) Any live cell with fewer than two live neighbours dies, as if caused \
           by underpopulation.\
        2) Any live cell with two or three live neighbours lives on to the next \
           generation.\
        3) Any live cell with more than three live neighbours dies, as if by\ 
           overpopulation.\
        4) Any dead cell with exactly three live neighbours becomes a live cell, \
           as if by reproduction. """
    ret = [numpy.zeros(self.width) for i in range(self.height)]
    for i in range(self.height):
      for j in range(self.width):
        scr, isAlive = self.score(i,j)
        if scr == 2 and isAlive:
          ret[i][j] = 1
        if scr == 3:
          ret[i][j] = 1
    self.grid = ret
