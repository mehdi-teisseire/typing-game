import pygame, time, random
from Player_class import Player
from Fruit_class import Fruit
from rules import *
from fruitsphysics import FruitPhysics
def game_start(screen, clock):
    running = True

    background = pygame.image.load('assets/background.png')
    background = pygame.transform.scale(background, (800, 600))
    
    last_fruit_spawn = time.time()
    SPAWN_INTERVAL = 0.7
    
    
    FRAMES = 60
    
    points = 0
    difficulty = "hard"

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
    physics = FruitPhysics(active_fruits, fruit_types)
    while running:
        current_time = time.time()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                points = 0
                number_fruit_before = len(active_fruits)
                for item in active_fruits:
                    if event.key == ord(item.letter):
                        points += item.effects(active_fruits, player)
                        active_fruits.remove(item)
                
                # active_fruits = [item for item in active_fruits if item.letter != event.key]
                player.score += points + points * 0.1 * (number_fruit_before-len(active_fruits))
        
        
        # Spawn new fruit every 3 seconds
        if current_time - last_fruit_spawn >= SPAWN_INTERVAL:
            # Choose random fruit type and create a new instance
            fruit_template = random.choice(fruit_types)
            # effect_template = random.choice(effect_types)
            
            match difficulty:
                case "endless":
                    pass
                case "easy":
                    new_fruit = Fruit(fruit_template.name, fruit_template.letter, fruit_template.image_path, fruit_template.path, fruit_template.effect, fruit_template.sound)
                case "normal":
                    pass
                case "hard":
                    new_fruit = Fruit(fruit_template.name, chr(random_letter()), fruit_template.image_path, fruit_template.path, fruit_template.effect, fruit_template.sound)
                    #change_invalid_letter(new_fruit, active_fruits)
                    
            active_fruits.append(new_fruit)
            last_fruit_spawn = current_time
        
        # Draw everything
        screen.blit(background, (0, 0))
        
        # Draw all active fruits
        for fruit in active_fruits:
            screen.blit(fruit.image, (fruit.x, fruit.y))
            screen.blit(fruit.letter_img, (fruit.x, fruit.y))

            if fruit.freeze > 0:
                fruit.stop_fruit()
            else:
                physics.move_fruits()
                physics.out_of_bounds()
            

        
        pygame.display.flip()
        clock.tick(FRAMES)
