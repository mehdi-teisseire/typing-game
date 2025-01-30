import pygame, random

def item_key_press(item):

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == item.letter:
                    item.effect()         

def random_letter():
    return random.randint(97,122)

def change_invalid_letter(new_fruit, active_fruits):
    if new_fruit.name == "bomb":
        for fruit in active_fruits:
            if fruit.letter == new_fruit.letter:
                new_fruit.letter = chr(random_letter())
                change_invalid_letter(new_fruit, active_fruits)
            else:
                return
    else:
        for fruit in active_fruits:
            if fruit.name == "bomb" and fruit.letter == new_fruit.letter:
                new_fruit.letter = chr(random_letter())
                change_invalid_letter(new_fruit, active_fruits)
            else:
                return