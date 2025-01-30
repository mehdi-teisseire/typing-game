import pygame, random

def item_key_press(item):

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == item.letter:
                    item.effect()
                   


def random_letter():
    return random.randint(97,122)


    
