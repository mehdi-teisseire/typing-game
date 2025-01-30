import pygame, random
import Player_class


class Fruit:  
    def __init__(self, name, letter, image_path, path, effect, sound):
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

        self.sound = sound

        self.x = 0 #physic[0] #curb_physic(self.x, self.y)[0] #random.randint(0, 750)  
        self.y = 600 #physic[1] #curb_physic(self.x, self.y)[1] #random.randint(0, 550)

        self.parabol_width = 0
        self.curb_center_x = 0
        self.curb_center_y = 0

        self.velocity_x = 5 #random.randint(7,10)

        self.paths()

        self.freeze = 0

    def effects(self, active_fruits, player, points):
        """Effect of each type of fruits on destroy"""
        match self.effect:
            case "points":
                points = self.effect_points()
            case "freeze":
                self.effect_freeze(player, active_fruits)
            case "bomb":
                self.effect_bomb(player)
        active_fruits.remove(self)
        return points

    def paths(self):
        """Path for fruit movements"""
        match self.path:
            case "linear":
                self.linear_path()
            case "curb":
                self.curb_path()
            case "sin":
                self.sin_path()
    
    def stop_fruit(self):
        self.x = self.x
        self.y = self.y
        self.freeze -= 1

    def effect_points(self):
        return 10

    def effect_freeze(self, player, active_fruits):
        """Freeze all fruits"""
        player.score -= 1
        print(player.score)
        for fruit in active_fruits:
            fruit.freeze = 1000

            
    def effect_bomb(self, player):
        player.lives -= 1
        print(player.lives)

    # Method about item movements
    def move_fruits(self):
        """ Fruit movement (should be in curb)"""
        self.y = self.parabol_width * ((self.x - self.curb_center_x) ** 2) + self.curb_center_y
        self.x += self.velocity_x

    def linear_path(self):
        self.path = self.path

    def curb_path(self):
        """Moves fruits following a x^2 curb"""
        self.parabol_width = 1 / random.randint(20, 800)
        self.curb_center_x = random.randint(200, 600)
        self.curb_center_y = random.randint(0, 200)

    def sin_path(self):
        self.path = self.path