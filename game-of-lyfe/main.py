import click
import gol
from time import sleep

@click.command()
@click.option('--width', default=10, help='Width of the grid.')
@click.option('--height', default=5, help='Height of the grid.')
@click.option('--glider', nargs=2, type=int,help="pass to get a glider at index passed after the glider flag")
@click.option('--herschel', nargs=2, type=int, help="pass to get a herschel glider at index passed after the herschel flag")
@click.option('--steps', default=15, help="set steps to specify how much the grid should evolve. ")

def main(width,height,glider,herschel,steps):
  """Simple program that greets NAME for a total of COUNT times."""
  g = gol.Grid(width,height)
  if len(glider) > 0:
    g.Glider(glider[0],glider[1])
  if len(herschel) > 0:
    g.Herschel(herschel[0], herschel[1])
  i = 0
  while steps==0 or i < steps:
    g.Print()
    g.Step()
    sleep(0.5)
    i += 1

if __name__ == '__main__':
    main()
