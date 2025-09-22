import pygame
from grid import grid

import os
os.environ["SDL_CIDEO_WINDOW_POS"] = "%d, %d" % (400,100)

surface = pygame.display.set_mode((1200,900))
pygame.display.set_caption("Sudoku")

pygame.font.init()
my_font = pygame.font.SysFont(name:"Comic Sans MS", size:50)
