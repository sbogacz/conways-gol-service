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
    for i in range(len(mask)):
      for j in range(len(mask[0])):
        m = i+(x%self.height)
        n = j+(y%self.width)
        self[m][n] = mask[i][j]   

  def __getitem__(self, item):
    return self.grid[item]

  def score(self, x, y):
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
    ret = [numpy.zeros(self.width) for i in range(self.height)]
    for i in range(self.height):
      for j in range(self.width):
        scr, isAlive = self.score(i,j)
        if scr == 2 and isAlive:
          ret[i][j] = 1
        if scr == 3:
          ret[i][j] = 1
    self.grid = ret
