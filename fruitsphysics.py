# fruitsphysics.py
import pygame, random

class FruitPhysics:
    '''Class for handling the physics of the fruits'''
    def __init__(self, active_fruits, fruit_types):
        self.active_fruits = active_fruits
        self.fruit_types = fruit_types
        
    def move_fruits(self, spawn_interval, current_interval, freezing):
        '''Moves the fruits and updates their position'''
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
                fruit.x += fruit.velocity_x *0.8

        for fruit in self.active_fruits:
            fruit.y += fruit.velocity_y
            fruit.velocity_y += random.randint(0, 1)
            fruit.x += fruit.velocity_x
            
    def out_of_bounds(self, player):
        '''Removes the fruits that are out of bounds'''
        for fruit in self.active_fruits[:]:
            if fruit.y > 600 or fruit.x > 810 or fruit.x < -5:
                self.active_fruits.remove(fruit)
                if fruit.name != "bomb" and fruit.name != "comet":
                    player.hearts -= 1
                