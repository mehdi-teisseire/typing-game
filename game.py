import pygame, time, random
from Player_class import Player
from Fruit_class import Fruit
from rules import *

def game_start(screen, clock, gameplay_surface, last_fruit_spawn, SPAWN_INTERVAL, FRAMES, fruit_types, difficulty, active_fruits):

        current_time = time.time()

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
                    failed = 0
                    new_fruit = Fruit(fruit_template.name, random_item_letter(fruit_template.name, active_fruits, failed), fruit_template.image_path, fruit_template.path, fruit_template.effect, fruit_template.sound)
                    
                    #change_invalid_letter(new_fruit, active_fruits)
                    
            if new_fruit.letter != "0":            
                active_fruits.append(new_fruit)
                last_fruit_spawn = current_time
        
        # Draw everything
        screen.blit(gameplay_surface, (50, 50))
        
        # Draw all active fruits
        for fruit in active_fruits:
            screen.blit(fruit.image, (fruit.x, fruit.y))
            screen.blit(fruit.letter_img, (fruit.x, fruit.y))

            if fruit.freeze > 0:
                fruit.stop_fruit()
            else:
                fruit.move_fruits()

        
        clock.tick(FRAMES)
