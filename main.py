from menu import run_menu


def main():
    run_menu()

if __name__ == "__main__" :
    main()


"""
import pygame
import random
import time

# Initialize the game
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
background = pygame.image.load('assets/background.png')
background = pygame.transform.scale(background, (800, 600))
last_fruit_spawn = time.time()
SPAWN_INTERVAL = 1

class Fruit:  
    def __init__(self, name, image_path):
        self.name = name
        self.image_path = image_path
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.x = random.randint(0, 750)  
        self.y = random.randint(0, 550)

# Create fruit templates
fruit_types = [
    Fruit('apple', 'assets/apple.png'),
    Fruit('banana', 'assets/banana.png'),
    Fruit('orange', 'assets/orange.png'),
    Fruit('watermelon', 'assets/watermelon.png'),
    Fruit('bomb', 'assets/bomb.png'),
    Fruit('coconut', 'assets/coconut.png'),

]

active_fruits = []  # List to store fruits currently on screen

while running:
    current_time = time.time()
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Spawn new fruit every 3 seconds
    if current_time - last_fruit_spawn >= SPAWN_INTERVAL:
        # Choose random fruit type and create a new instance
        fruit_template = random.choice(fruit_types)
        new_fruit = Fruit(fruit_template.name, fruit_template.image_path)
        active_fruits.append(new_fruit)
        last_fruit_spawn = current_time
    
    # Draw everything
    screen.blit(background, (0, 0))
    
    # Draw all active fruits
    for fruit in active_fruits:
        screen.blit(fruit.image, (fruit.x, fruit.y))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

"""