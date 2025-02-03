import pygame
import random
import time
from menu import run_menu
from utils import draw_button, draw_glitched_title

pygame.init()



# Function to save name to a text file
def save_name_to_file(name):
    """Append the name to a text file."""
    with open("scores.txt", "a", encoding='utf-8') as file:
        file.write(name + "\n")

# Laser parameters, moves, and draw
class Laser:
    """ Laser parameters, moves, and draw"""
    def __init__(self, x, y, target_x, target_y):
        self.x = x
        self.y = y
        self.speed = 5

        delta_x = target_x - x
        delta_y = target_y - y
        distance = (delta_x**2 + delta_y**2) ** 0.5
        self.dir_x = (delta_x / distance) * self.speed
        self.dir_y = (delta_y / distance) * self.speed
        self.rect = pygame.Rect(self.x, self.y, 5, 10) 

    def move(self):
        self.x += self.dir_x 
        self.y += self.dir_y  
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect) 

# The synopsis of the game
def draw_synopsis(screen):
    """ The synopsis of the game """
    synopsis_text = [
        "In a funny universe ",
        "where fruits can talk,",
        "a brave group of fruity,",
        "friends decides ",
        "to take over space,",
        "hoping to rule new worlds.",
        "But their plans quickly ",
        "go wrong when they make",
        "some angry aliens mad",
        "about the fruity invasion",
        "of their home.",
        "As these brave fruits try to,",
        "escape from falling",
        "rocks and space dangers,",
        "they find themselves",
        "in big trouble,",
        "chased by the aliens.",
        "Will they learn that ",
        "not all dreams are easy",
        "to reach, or will their",
        "fruity plans end ",
        "in a tasty snack?",
    ]

    font = pygame.font.Font("media/font/Conthrax.otf", 22)
    text_surface = []
    for line in synopsis_text:
        text_surface.append(font.render(line, True, (255, 255, 255)))

    rect_width = 435
    rect_height = 640
    rect_x = 50
    rect_y = 30
    pygame.draw.rect(screen, (0, 0, 0), (rect_x, rect_y, rect_width, rect_height))  
    pygame.draw.rect(screen, (255, 255, 255), (rect_x, rect_y, rect_width, rect_height), 4)  
    
    line_spacing = 28 
    for i, text in enumerate(text_surface):        
        screen.blit(text, (rect_x + 10, rect_y + 10 + i * line_spacing))

# To draw the strawberry
def draw_strawberry(screen, strawberry_image, strawberry_x, strawberry_y):
    """ to draw the strawberry """
    screen.blit(strawberry_image, (strawberry_x, strawberry_y))

# to update the strawberry positon
def update_strawberry_position(strawberry_x, strawberry_y, strawberry_speed_x, 
                               strawberry_speed_y, new_strawberry_width, desired_strawberry_height):
    """  to update the strawberry positon """
    strawberry_x += strawberry_speed_x
    strawberry_y += strawberry_speed_y

    if strawberry_x <= 0 or strawberry_x >= 1350 - new_strawberry_width:
        strawberry_speed_x *= -1
    if strawberry_y <= 0 or strawberry_y >= 700 - desired_strawberry_height:
        strawberry_speed_y *= -1

    return strawberry_x, strawberry_y, strawberry_speed_x, strawberry_speed_y

# to reset the strawberry position
def reset_strawberry_position(new_strawberry_width, new_strawberry_height):
    """ to reset the strawberry position """
    strawberry_x = random.randint(0, 1350 - new_strawberry_width)
    strawberry_y = random.randint(0, 700 - new_strawberry_height)
    return strawberry_x, strawberry_y
 
# to update the saucer position
def update_saucer_position(saucer_x, saucer_y, strawberry_x, strawberry_y):
    """to update the saucer position """
    saucer_distance = 30
    if abs(saucer_x - strawberry_x) > saucer_distance or abs(saucer_y - strawberry_y) > saucer_distance:
        if saucer_x < strawberry_x:
            saucer_x += 1
        else:
            saucer_x -= 1
        if saucer_y < strawberry_y:
            saucer_y += 1
        else:
            saucer_y -= 1
    return saucer_x, saucer_y

# to load the assets
def load_assets():
    """ to load assets images background """
    background_image = pygame.image.load("media/background/star-background.jpg") 
    background_image = pygame.transform.scale(background_image, (1350, 700)) 

    strawberry_image = pygame.image.load("media/images/strawberry.png") 
    original_strawberry_width, original_strawberry_height = strawberry_image.get_size()
    desired_strawberry_height = 50  
    strawberry_scaling_factor = desired_strawberry_height / original_strawberry_height
    new_strawberry_width = int(original_strawberry_width * strawberry_scaling_factor)
    strawberry_image = pygame.transform.scale(strawberry_image, (new_strawberry_width, 
                                                                 desired_strawberry_height))

    saucer_image = pygame.image.load("media/images/flying_saucer.png")  
    original_saucer_width, original_saucer_height = saucer_image.get_size()
    desired_saucer_height = 150  
    saucer_scaling_factor = desired_saucer_height / original_saucer_height
    new_saucer_width = int(original_saucer_width * saucer_scaling_factor)
    saucer_image = pygame.transform.scale(saucer_image, (new_saucer_width, 
                                                         desired_saucer_height))

    click_sound = pygame.mixer.Sound("media/sounds/old-radio-button-click.mp3") # change ?

    font = pygame.font.Font("media/font/Conthrax.otf", 20) 
    title_font = pygame.font.Font("media/font/BTTF.ttf", 45)
    large_font = pygame.font.Font("media/font/BTTF.ttf", 60)

    return (background_image, strawberry_image, new_strawberry_width, 
            saucer_image, new_saucer_width, click_sound, font, title_font, 
            large_font)

# main function 
def lore_menu():
    pygame.init()

    screen = pygame.display.set_mode((1350, 700))
    pygame.display.set_caption("Space Fruits Invaders - the legend begins here!")


    (background_image, strawberry_image, new_strawberry_width, 
     saucer_image, new_saucer_width, click_sound, 
     font, title_font, large_font) = load_assets()
    
    desired_strawberry_height = 50  
    desired_saucer_height = 150  

    strawberry_x, strawberry_y = reset_strawberry_position(new_strawberry_width, 
                                                           desired_strawberry_height)
    strawberry_speed_x = random.choice([-1, 1]) 
    strawberry_speed_y = random.choice([-1, 1]) 

    saucer_x = random.randint(0, 1350 - new_saucer_width)
    saucer_y = random.randint(0, 700 - desired_saucer_height)

    lasers = []  
    explosion_parts = []
    
    button_color = (0, 128, 0)
    button_hover = (0, 225, 0)
    shadow_color = (0, 80, 0)

    name_input_rect = pygame.Rect(500, 580, 300, 50)  
    name_input_color = (255, 255, 255)  
    name_input_text = ""
    entered_name_message = ""  

    instruction_text = [
        "To register your score", 
        "enter your name:"
    ]

    running = True
    buttons = [
        {"text": "CONTINUE", "position": (1100, 610)},
    ]

    clock = pygame.time.Clock()  

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE: 
                    name_input_text = name_input_text[:-1]
                elif event.key == pygame.K_RETURN:
                    save_name_to_file(name_input_text) # for the score player name
                    entered_name_message = f"Name entered: {name_input_text}"
                    name_input_text = ""  
                else:
                    name_input_text += event.unicode 

            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    button_rectangle = draw_button(screen, button['text'], 
                                                   button['position'], (150, 50), 
                                                   button_color, button_hover, 
                                                   shadow_color, font)
                    if button_rectangle.collidepoint(event.pos):
                        click_sound.play()
                        if button['text'] == "CONTINUE":
                            run_menu()  

        screen.blit(background_image, (0, 0))
        draw_synopsis(screen) 

        strawberry_x, strawberry_y, strawberry_speed_x, strawberry_speed_y = update_strawberry_position(strawberry_x, strawberry_y, strawberry_speed_x, strawberry_speed_y, new_strawberry_width, desired_strawberry_height)

        if abs(saucer_x - strawberry_x) < 150 and random.random() < 0.02:  
            lasers.append(Laser(saucer_x + new_saucer_width // 2, saucer_y, 
                                strawberry_x + new_strawberry_width // 2, strawberry_y))

        for laser in lasers[:]:
            laser.move() 
            if laser.y < 0: 
                lasers.remove(laser)
            else:
                laser.draw(screen)

                if laser.rect.colliderect(pygame.Rect(strawberry_x, strawberry_y, 
                                                      new_strawberry_width, desired_strawberry_height)):
                    explosion_parts.extend([[strawberry_x + new_strawberry_width // 2 + random.randint(-25, 25), 
                                             strawberry_y + desired_strawberry_height // 2 + random.randint(-25, 25), 
                                             random.randint(-2, 2), 
                                             random.randint(-5, 0), 
                                             time.time()] for _ in range(10)]) 
                    lasers.remove(laser)
                    strawberry_x, strawberry_y = reset_strawberry_position(new_strawberry_width, desired_strawberry_height)

        draw_strawberry(screen, strawberry_image, strawberry_x, strawberry_y)

        saucer_x, saucer_y = update_saucer_position(saucer_x, saucer_y, strawberry_x, strawberry_y)

        screen.blit(saucer_image, (saucer_x, saucer_y))

        current_time = time.time()  
        for part in explosion_parts[:]:
            part[0] += part[2] 
            part[1] += part[3]  
            
            if part[1] > 700 or part[0] < 0 or part[0] > 1350 or (current_time - part[4]) > 5:  
                explosion_parts.remove(part)
            else:
                pygame.draw.circle(screen, (255, 165, 0), (part[0], part[1]), 5)  

        text_lines = ["Welcome &", "SPACE FRUITS", "INVADERS!!!"]
        draw_glitched_title(screen, text_lines,"&", large_font, (650, 50), title_font)  

        for button in buttons:
            draw_button(screen, button['text'], button['position'], (150, 55), 
                        button_color, button_hover, shadow_color, font)

        pygame.draw.rect(screen, name_input_color, name_input_rect)  

        input_text_surface = font.render(name_input_text, True, (0, 0, 0))  
        screen.blit(input_text_surface, (name_input_rect.x + 10, name_input_rect.y + 10))  

        for i, line in enumerate(instruction_text):
            instruction_surface = font.render(line, True, (255, 255, 255))
            screen.blit(instruction_surface, (name_input_rect.x + 10, name_input_rect.y - 50 + (i * 20)))

        if entered_name_message:  
            entered_message_surface = font.render(entered_name_message, True, (255, 255, 255)) 
            screen.blit(entered_message_surface, (500, 640))  

        pygame.display.flip()
        clock.tick(60) 

    pygame.quit()