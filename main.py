import pygame, random, time, os
from rules import *
from Fruit_class import Fruit
from Player_class import Player

# Initialize the game
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
background = pygame.image.load('assets/background.png')
background = pygame.transform.scale(background, (800, 600))
last_fruit_spawn = time.time()
SPAWN_INTERVAL = 0.5
FRAMES = 60
points = 0

# Create new player
player = Player("Aaa", 0, 3)

# Create fruit templates
fruit_types = [ 
    Fruit('apple', 'a', 'assets/apple.png', 'curb', 'points', 'test.ogg'),
    Fruit('banana', 'b', 'assets/banana.png', 'curb', 'points', 'test.ogg'),
    Fruit('orange', 'o', 'assets/orange.png', 'curb', 'points', 'test.ogg'),
    Fruit('watermelon', 'w', 'assets/watermelon.png', 'curb', 'points', 'test.ogg'),
    Fruit('comet', 'i', 'assets/explosion.png', 'sin', 'freeze', 'test.ogg'),
    Fruit('bomb', 'e', 'assets/bomb.png', 'linear', 'bomb', 'test.ogg')
]

active_fruits = []  # List to store fruits currently on screen        

while running:
    current_time = time.time()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            number_fruit_before = len(active_fruits)
            for item in active_fruits:
                if event.key == ord(item.letter):
                    points += item.effects(active_fruits, player, points)
            player.score += points * (number_fruit_before-len(active_fruits)) * 1.5
            points = 0
            print(number_fruit_before-len(active_fruits))
      
    
    # Spawn new fruit every 3 seconds
    if current_time - last_fruit_spawn >= SPAWN_INTERVAL:
        # Choose random fruit type and create a new instance
        fruit_template = random.choice(fruit_types)
        # effect_template = random.choice(effect_types)
        
        # Easy
        new_fruit = Fruit(fruit_template.name, fruit_template.letter, fruit_template.image_path, fruit_template.path, fruit_template.effect, fruit_template.sound)
        # Hard
        # new_fruit = Fruit(fruit_template.name, chr(random_letter()), fruit_template.image_path, fruit_template.path, fruit_template.effect, fruit_template.sound)
        
        active_fruits.append(new_fruit)
        last_fruit_spawn = current_time
    
    # Draw everything
    screen.blit(background, (0, 0))
    
    # Draw all active fruits
    for fruit in active_fruits:
        screen.blit(fruit.image, (fruit.x, fruit.y))
        screen.blit(fruit.letter_img, (fruit.x, fruit.y))
        fruit.move_fruits()
    
    pygame.display.flip()
    clock.tick(FRAMES)

pygame.quit()