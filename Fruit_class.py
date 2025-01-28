import pygame, random
from rules import *


class Fruit:  
    def __init__(self, name, letter, image_path, path, effect):
        self.name = name
        self.letter = letter
        self.letter_path = f"assets/letters/{letter}.png"
        self.letter_img = pygame.image.load(self.letter_path)
        self.letter_img = pygame.transform.scale(self.letter_img, (50, 50))

        self.image_path = image_path
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (50, 50))
        
        self.path = path
        self.effect = effect

        self.x = random.randint(0,750) #physic[0] #curb_physic(self.x, self.y)[0] #random.randint(0, 750)  
        self.y = 550 #physic[1] #curb_physic(self.x, self.y)[1] #random.randint(0, 550)

    def effects(self, active_fruits, player):
        match self.effect:
            case "points":
                effect_points(self, player)
            case "freeze":
                effect_freeze(self, player)
            case "bomb":
                effect_bomb(self, player)
        active_fruits.remove(self)

    def paths(self):
        match self.path:
            case "linear":
                linear_path(self)
            case "curb":
                curb_path(self)
            case "sin":
                sin_path(self)