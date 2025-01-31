# fruitsphysics.py
import pygame, random

class FruitPhysics:
    def __init__(self, active_fruits, fruit_types):
        self.active_fruits = active_fruits
        self.fruit_types = fruit_types
        
    def move_fruits(self):
        for fruit in self.active_fruits:
            fruit.y += fruit.velocity_y
            fruit.velocity_y += random.randint(0, 1)
            fruit.x += fruit.velocity_x
            
    def out_of_bounds(self, player):
        for fruit in self.active_fruits[:]:
            if fruit.y > 600 or fruit.x > 805 or fruit.x < -5:
                self.active_fruits.remove(fruit)
                #player.hearts -= 1
                print('Fruit out of bounds')
                
    def destroy_fruits(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            for fruit in self.active_fruits[:]:
                if self.fruit_types[4].name == fruit.name:
                    print('Game Over')
                    pygame.quit()