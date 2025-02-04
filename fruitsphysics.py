# fruitsphysics.py
import pygame, random

class FruitPhysics:
    def __init__(self, active_fruits, fruit_types):
        self.active_fruits = active_fruits
        self.fruit_types = fruit_types
        
    def move_fruits(self, spawn_interval, current_interval, freezing):
        for fruit in self.active_fruits:
            if fruit.freeze > 0:
                if not freezing[0]:
                    current_interval[0] = spawn_interval[0]
                    spawn_interval[0] = 1000000
                    freezing[0] = True
                fruit.stop_fruit()
            else:
                if freezing[0]:
                    spawn_interval[0] = current_interval[0]
                    freezing[0] = False
                fruit.y += fruit.velocity_y
                fruit.velocity_y += random.randint(0, 1)
                fruit.x += fruit.velocity_x *0.5
            
    def out_of_bounds(self, player):
        for fruit in self.active_fruits[:]:
            if fruit.y > 600 or fruit.x > 805 or fruit.x < -5:
                self.active_fruits.remove(fruit)
                if fruit.name != "bomb" and fruit.name != "comet":
                    player.hearts -= 1
                #print('Fruit out of bounds')
                
    def destroy_fruits(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            for fruit in self.active_fruits[:]:
                if self.fruit_types[4].name == fruit.name:
                    print('Game Over')
                    pygame.quit()