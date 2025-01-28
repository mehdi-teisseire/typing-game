import pygame, random
from Player_class import Player

player = Player("Aaa", 0, 1)

def item_key_press(item):

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == item.letter:
                    item.effect()


def random_letter():
    return random.randint(97,122)

def effect_points(self):
    player.score += 10
    print(player.score)

def effect_freeze(self):
    player.score -= 1
    print(player.score)
            
def effect_bomb(self):
    player.lives -= 1
    print(player.lives)
    
def linear_path(self):
    pass

def curb_path(self):
    pass

def sin_path(self):
    pass