import pygame, random


class Fruit:  
    def __init__(self, name, letter, image_path, effect, sound):
        self.random_value= random.randint(0,50)
        
        self.name = name
        self.letter = letter
        self.letter_path = f"media/assets/letters/{letter}.png"
        self.letter_img = pygame.image.load(self.letter_path)
        self.letter_img = pygame.transform.scale(self.letter_img, (30+self.random_value*0.5, 30+self.random_value*0.5))

        self.image_path = image_path
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (50+self.random_value, 50+self.random_value))
        
        self.effect = effect

        self.sound = sound

        self.x = random.randint(100, 650)  
        self.y = 600
        self.velocity_x = random.randint(-1, 1)
        self.velocity_y = random.randint(-22, -20)

        self.freeze = 0

    def effects(self, active_fruits, player):
        """Effect of each type of fruits on destroy"""
        match self.effect:
            case "points":
                return self.effect_points()
            case "freeze":
                return self.effect_freeze(player, active_fruits)
            case "bomb":
                return self.effect_bomb(player)

    def stop_fruit(self):
        self.x = self.x
        self.y = self.y
        self.freeze -= 1

    def effect_points(self):
        return 10

    def effect_freeze(self, player, active_fruits):
        """Freeze all fruits"""
        freeze_sound = pygame.mixer.Sound("media/sounds/freeze.wav")
        freeze_sound.play()
        for fruit in active_fruits:
            fruit.freeze = 100
        return 0 #-1
            
    def effect_bomb(self, player):
        bomb_sound = pygame.mixer.Sound("media/sounds/bomb.wav")
        health_sound = pygame.mixer.Sound("media/sounds/health.wav")
        health_sound.play()
        bomb_sound.play()
        player.hearts -= 1
        return 0



