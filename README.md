# Python Practice Esoterica

This repository is intended to hold the odds and ends of the small side projects I'm using to brush up (or really, finally learn) my Python for use in the Deep Learning course that I'm taking. I make no promises nor guarantees aout any of the code that may appear here. I've written it purely for personal use, and as such it isnot build with resiliency or scale in mind. Please bear this in mind if you choose to play around with any of the code found in this repository.

## Game-of-lyfe

This folder contains a small cli implementation of Conway's Game of Life. It uses the click library for cli option support, and numpy to import arrays (and the zeros function). It supports the following flags
	* `width`: to configure the grid width
	* `height`: to configure the grid height
	* `steps`: to configure the number of steps in the game of life evolution
	* `glider`: takes two integer indices and sets up a glider starting at those indices
	* `herschel`: functions like glider, but for the herschel exploder

Example Usage:

```sh
python main.py --width 40 --height 20 --herschel 5 5 --glider 10 10 --steps 0
```
