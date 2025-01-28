import pygame, random, time
from rules import *







# Initialize the game
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
background = pygame.image.load('assets/background.png')
background = pygame.transform.scale(background, (800, 600))
last_fruit_spawn = time.time()
SPAWN_INTERVAL = 1



class Fruit:  
    def __init__(self, name, letter, image_path, path, effect):
        self.name = name
        self.letter = letter

        self.image_path = image_path
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (50, 50))
        
        self.path = path
        self.effect = effect

        self.x = 0 #physic[0] #curb_physic(self.x, self.y)[0] #random.randint(0, 750)  
        self.y = 0 #physic[1] #curb_physic(self.x, self.y)[1] #random.randint(0, 550)

    def effects(self):
        match self.effect:
            case "points":
                effect_points(self)
            case "freeze":
                effect_freeze(self)
            case "bomb":
                effect_bomb(self)
        active_fruits.remove(self)

    def paths(self):
        match self.path:
            case "linear":
                linear_path(self)
            case "curb":
                curb_path(self)
            case "sin":
                sin_path(self)

# Create fruit templates
fruit_types = [ 
    Fruit('apple', 'a', 'assets/apple.png', 'curb', 'points'),
    Fruit('banana', 'b', 'assets/banana.png', 'curb', 'points'),
    Fruit('orange', 'o', 'assets/orange.png', 'curb', 'points'),
    Fruit('watermelon', 'w', 'assets/watermelon.png', 'curb', 'points'),
    Fruit('ice', 'i', 'assets/explosion.png', 'sin', 'freeze'),
    Fruit('bomb', 'z', 'assets/bomb.png', 'linear', 'bomb')
]
active_fruits = []  # List to store fruits currently on screen

while running:
    current_time = time.time()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            for item in active_fruits:
                if event.key == ord(item.letter):
                    item.effects()
      
    
    # Spawn new fruit every 3 seconds
    if current_time - last_fruit_spawn >= SPAWN_INTERVAL:
        # Choose random fruit type and create a new instance
        fruit_template = random.choice(fruit_types)
        # effect_template = random.choice(effect_types)
        #new_fruit = Fruit(fruit_template.name, fruit_template.letter, fruit_template.image_path, fruit_template.path, fruit_template.effect)
        new_fruit = Fruit(fruit_template.name, chr(random_letter()), fruit_template.image_path, fruit_template.path, fruit_template.effect)
        active_fruits.append(new_fruit)
        last_fruit_spawn = current_time
    
    # Draw everything
    screen.blit(background, (0, 0))
    
    # Draw all active fruits
    for fruit in active_fruits:
        screen.blit(fruit.image, (fruit.x, fruit.y))
        screen.blit(fruit.image, (fruit.x, fruit.y))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()