import pygame
import game

# Initialize the game
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

game.game_start(screen, clock)

pygame.quit()