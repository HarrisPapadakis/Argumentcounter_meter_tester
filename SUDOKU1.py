import pygame

surface = pygame.display.set_mode((1200, 900))
pygame.display.set_caption("Sudoku")

running = True

while running:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False 