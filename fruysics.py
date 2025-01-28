import random, pygame, time
from main import *

def delete_fruits():
    for fruit in active_fruits:
        fruit.y += 1
        if fruit.y > 600:
            active_fruits.remove(fruit)
            print('Fruit removed')