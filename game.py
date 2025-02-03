import pygame, time, random
from Player_class import Player
from Fruit_class import Fruit
from rules import *
from fruitsphysics import FruitPhysics

def game_start(screen, gameplay_surface, last_fruit_spawn, spawn_interval, fruit_types, difficulty, active_fruits, physics, player):
        """Draw game window and spawn items"""
        current_time = pygame.time.get_ticks()
        # Spawn new fruit every 3 seconds
        if current_time - last_fruit_spawn[0] >= spawn_interval[0]:
            # Choose random fruit type and create a new instance
                   
            match difficulty:
                case "endless":
                    player.hearts = -1
                    fruit_template = random.choice(fruit_types)
                    new_fruit = Fruit(fruit_template.name, fruit_template.letter, fruit_template.image_path, fruit_template.path, fruit_template.effect, fruit_template.sound)
                case "easy":
                    fruit_template = random.choice(fruit_types)
                    new_fruit = Fruit(fruit_template.name, fruit_template.letter, fruit_template.image_path, fruit_template.path, fruit_template.effect, fruit_template.sound)
                case "normal":
                    fruit_template = random.choice(fruit_types)

                    spawn_interval[0] *= 0.9999

                    failed = 0
                    new_fruit = Fruit(fruit_template.name, random_item_letter(fruit_template.name, active_fruits, failed), fruit_template.image_path, fruit_template.path, fruit_template.effect, fruit_template.sound)
                    

                    if new_fruit.letter != "0":     
                        active_fruits.append(new_fruit)
                        last_fruit_spawn[0] = pygame.time.get_ticks() #current_time
                case "hard":
                    for i in range(2):
                        fruit_template = random.choice(fruit_types) #fruit_template = random.choice(fruit_types[5:])
                        
                        spawn_interval[0] *= 0.999
                        
                        failed = 0
                        new_fruit = Fruit(fruit_template.name, random_item_letter(fruit_template.name, active_fruits, failed), fruit_template.image_path, fruit_template.path, fruit_template.effect, fruit_template.sound)


                        if new_fruit.letter != "0":     
                            active_fruits.append(new_fruit)
                            last_fruit_spawn[0] = pygame.time.get_ticks() #current_time
                

        # Draw everything
        screen.blit(gameplay_surface, (50, 50))
        
        # Draw all active fruits
        for fruit in active_fruits:
            screen.blit(fruit.image, (fruit.x, fruit.y))
            screen.blit(fruit.letter_img, (fruit.x, fruit.y))

            if fruit.freeze > 0:
                fruit.stop_fruit()
            else:
                FruitPhysics.move_fruits(physics)

        FruitPhysics.out_of_bounds(physics, player)

        
