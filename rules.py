import random

def random_letter():
    return random.randint(97,122)

def random_item_letter(name, active_fruits, failed):
    temp_letter = chr(random_letter())
    failed = 0
    if name == "bomb":
        for fruit in active_fruits:
            if fruit.letter == temp_letter:
                failed = 1
                break
            else:
                continue
    else:
        for fruit in active_fruits:
            if fruit.name == "bomb" and fruit.letter == temp_letter:
                failed = 1
                break
            else:
                continue
    
    if failed > 5:
        return "0"
    
    if failed:
        temp_letter = random_item_letter(name, active_fruits)

    return temp_letter