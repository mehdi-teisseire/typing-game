import pygame
import menu

# Initialize the game
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

menu.run_menu(clock)

pygame.quit()