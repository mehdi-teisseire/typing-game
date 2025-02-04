import pygame, random
from rules import *
from Fruit_class import Fruit
from fruitsphysics import *
from menu import run_menu
from utils import draw_glitched_title, create_transparent_button
#from settings import draw_settings


pygame.init()

# Function to save name to a text file
def save_score_to_file(player):
    """Append the name to a text file."""
    with open("scores.txt", "a", encoding='utf-8') as file:
        file.write(player.name + ", " + str(player.score) + "\n")
        player.score_upload = True
    
        
# To display the gameplay
def draw_gameplay(screen, last_fruit_spawn, spawn_interval, current_interval, fruit_types, difficulty, active_fruits, physics, player, freezing):
    """ The gameplay area """
    gameplay_surface = pygame.Surface((800, 600))
    gameplay_surface = pygame.image.load("media/background/star-background.jpg")
    gameplay_surface = pygame.transform.scale(gameplay_surface, (800, 600))
    border_color = (255, 255, 255) 
    pygame.draw.rect(gameplay_surface, border_color, (0, 0, 800, 600), 4) 
    
    heart_icon = pygame.image.load("media/icons/heart.png")
    heart_icon = pygame.transform.scale(heart_icon, (25, 25))
    for index in range(player.hearts):
        gameplay_surface.blit(heart_icon, (10 + index * 30, 10))

    star_icon = pygame.image.load("media/icons/star.png")
    star_icon = pygame.transform.scale(star_icon, (25,25))
    gameplay_surface.blit(star_icon, (670, 10))
    font = pygame.font.Font("media/font/Conthrax.otf", 20)
    score_surface = font.render(f"{player.score}", True, (255, 255, 255))
    gameplay_surface.blit(score_surface, (700, 11))

    """Draw game window and spawn items"""
    current_time = pygame.time.get_ticks()
    # Spawn new fruit every 3 seconds
    if current_time - last_fruit_spawn[0] >= spawn_interval[0]:
        # Choose random fruit type and create a new instance
               
        match difficulty:
            case "ENDLESS":
                fruit_template = random.choice(fruit_types)
                spawn_interval[0] *= 0.99
                failed = 0
                new_fruit = Fruit(fruit_template.name,  random_item_letter(fruit_template.name, active_fruits, failed), fruit_template.image_path, fruit_template.effect, fruit_template.sound)

                if new_fruit.letter != "0":     
                    active_fruits.append(new_fruit)
                    last_fruit_spawn[0] = pygame.time.get_ticks() #current_time
            case "EASY":
                fruit_template = random.choice(fruit_types)
                new_fruit = Fruit(fruit_template.name, fruit_template.letter, fruit_template.image_path, fruit_template.effect, fruit_template.sound)
            
                active_fruits.append(new_fruit)
                last_fruit_spawn[0] = pygame.time.get_ticks() #current_time
            case "NORMAL":
                fruit_template = random.choice(fruit_types)
                spawn_interval[0] *= 0.999
                failed = 0
                new_fruit = Fruit(fruit_template.name, random_item_letter(fruit_template.name, active_fruits, failed), fruit_template.image_path, fruit_template.effect, fruit_template.sound)
                
                if new_fruit.letter != "0":     
                    active_fruits.append(new_fruit)
                    last_fruit_spawn[0] = pygame.time.get_ticks() #current_time
            case "HARD":
                for i in range(random.randint(1,3)):
                    fruit_template = random.choice(fruit_types[5:])
                    
                    spawn_interval[0] *= 0.99
                    
                    failed = 0
                    new_fruit = Fruit(fruit_template.name, random_item_letter(fruit_template.name, active_fruits, failed), fruit_template.image_path, fruit_template.effect, fruit_template.sound)
                    
                    if new_fruit.letter != "0":     
                        active_fruits.append(new_fruit)
                        last_fruit_spawn[0] = pygame.time.get_ticks() #current_time
                

    
    screen.blit(gameplay_surface, (50, 50))

       # Draw all active fruits
    for fruit in active_fruits:
        screen.blit(fruit.image, (fruit.x, fruit.y))
        screen.blit(fruit.letter_img, (fruit.x + 10 + fruit.random_value * 0.4, fruit.y-50))


        FruitPhysics.move_fruits(physics, spawn_interval, current_interval, freezing)

    FruitPhysics.out_of_bounds(physics, player)

# General function for the game 
def gameplay(background_path, alien_image_path, difficulty, player):
    """General function for the game """
    screen = pygame.display.set_mode((1350, 700))
    pygame.display.set_caption(f"Space Fruits Invaders - Difficulty: {difficulty}")

    background_image = pygame.image.load(background_path)
    background_image = pygame.transform.scale(background_image, (1350, 700))
   
    png_image = pygame.image.load(alien_image_path)
    original_width, original_height = png_image.get_size()
    desired_width = 400
    scaling_factor = desired_width / original_height
    new_height = int(original_width * scaling_factor)
    
    png_image = pygame.transform.scale(png_image, (new_height, desired_width))
    pygame.mixer.music.load('media/sounds/Heian Alien.mp3')
    pygame.mixer.music.play(-1)
    click_sound = pygame.mixer.Sound("media/sounds/clickbutton.wav")

    font = pygame.font.Font("media/font/Conthrax.otf", 20)
    title_font = pygame.font.Font("media/font/BTTF.ttf", 45)
    large_font = pygame.font.Font("media/font/BTTF.ttf", 70)
    play_pause_font = pygame.font.Font("media/font/icons.ttf", 30)
    home_font = pygame.font.Font("media/font/alienato.TTF", 55)
    settings_font = pygame.font.Font("media/font/Other_Space.ttf", 55)

    button_color = (0, 0, 0)  
    alpha_value_transparent = 0  
    alpha_value_visible = 100     
    button_D_color = (0, 255, 0)  
    button_C_color = (255, 0, 0)  
    button_L_color = (0, 0, 0)

    buttons = [
        {"text": "NORMAL", "position": (1010, 510)},
        {"text": "HARD", "position": (1180, 510)},
        {"text": "ENDLESS", "position": (1010, 555)},
        {"text": "EASY", "position": (1180, 555)},
        {"text": "D", "position": (1005, 620)},
        {"text": "C", "position": (1085, 620)},
        {"text": "L", "position": (1165, 620)},
        {"text": "U", "position": (1235, 620)}, 
    ]
   
    running_game = True
    pressed_button = None  
    selected_level = None
    selected_language = "Select Language"
    dropdown_open = False  

    # Game Variable
    last_fruit_spawn = [pygame.time.get_ticks()]
    spawn_interval = [2000]
    current_interval = [0]

    freezing = [False]
    
    points = 0

    # Create fruit templates
    fruit_types = [ 
        Fruit('apple', 'a', 'media/assets/apple.png', 'points', 'test.ogg'),
        Fruit('banana', 'b', 'media/assets/banana.png', 'points', 'test.ogg'),
        Fruit('lemon', 'l', 'media/assets/lemon.png', 'points', 'test.ogg'),
        Fruit('lime', 'i', 'media/assets/lime.png', 'points', 'test.ogg'),
        Fruit('orange', 'o', 'media/assets/orange.png', 'points', 'test.ogg'),
        Fruit('pear', 'p', 'media/assets/pear.png', 'points', 'test.ogg'),
        Fruit('pomegranate', 'g', 'media/assets/pomegranate.png', 'points', 'test.ogg'),
        Fruit('raspberry', 'r', 'media/assets/raspberry.png', 'points', 'test.ogg'),
        Fruit('watermelon', 'w', 'media/assets/watermelon.png', 'points', 'test.ogg'),
        Fruit('strawberry', 's', 'media/assets/banana.png', 'points', 'test.ogg'),
        Fruit('comet', 'c', 'media/assets/meteor3.png', 'freeze', 'test.ogg'),
        Fruit('bomb', 'z', 'media/assets/bomb.png', 'bomb', 'test.ogg')
    ]

    active_fruits = []  # List to store fruits currently on screen
         

    physics = FruitPhysics(active_fruits, fruit_types)
    clock = pygame.time.Clock()

    while running_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_game = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, button in enumerate(buttons):
                    button_surface, button_rectangle = create_transparent_button(
                        button['text'],
                        button['position'],
                        (55, 55) if button['text'] in ['D', 'C', 'L'] else (90, 55) 
                        if button['text'] == "U" else (150, 55),
                        button_D_color if button['text'] == "D" else button_C_color if button['text'] == "C" 
                        else button_L_color if button['text'] == 'L' else button_color,
                        alpha_value_visible if button['text'] in ['D', 'C'] else alpha_value_transparent, 
                        play_pause_font if button['text'] in ["D", "C"] else home_font if button['text'] == 'L' 
                        else settings_font if button['text'] == 'U' else font
                    )
                    
                    if button_rectangle.collidepoint(event.pos):
                        click_sound.play() 

                        if button["text"] in ['NORMAL', 'EASY', 'ENDLESS', 'HARD']:
                            selected_level = button["text"]  
                            return selected_level  
                        elif button['text'] == "L":            
                            run_menu(player)             
                            return
                        #elif button ['text'] == "U":
                            #draw_settings()                    
                            #break
                        pressed_button = i        
                        break

            if event.type == pygame.MOUSEBUTTONUP:
                pressed_button = None  

            # Game events
            if event.type == pygame.KEYDOWN:
                points = 0
                number_fruit_before = len(active_fruits)
                for item in active_fruits[:]:
                    if event.key == ord(item.letter):
                        points += item.effects(active_fruits, player)
                        active_fruits.remove(item)
                
                player.score += round(points * (number_fruit_before-len(active_fruits)))

        screen.blit(background_image, (0, 0)) 
        
        png_rectangle = png_image.get_rect(right=1350, top=100)
        screen.blit(png_image, png_rectangle)
        mouse_position = pygame.mouse.get_pos()
        if png_rectangle.collidepoint(mouse_position):
            shake_offset = random.randint(-5, 5)
            screen.blit(png_image, (png_rectangle.x + shake_offset, png_rectangle.y))
        else:
            screen.blit(png_image, png_rectangle)

        text_lines = [difficulty]  
        draw_glitched_title(screen, text_lines, difficulty[0], large_font, (925, 40), title_font)

        menu_background_rect_width = 375
        menu_background_rect_height = 200
        menu_background_rect_surface = pygame.Surface((menu_background_rect_width, 
                                                       menu_background_rect_height), pygame.SRCALPHA) 
        black_color = (0, 0, 0, 128)  
        menu_background_rect_surface.fill(black_color)
        border_color = (255, 255, 255) 
        pygame.draw.rect(menu_background_rect_surface, border_color, (0, 0, menu_background_rect_width, 
                                                                      menu_background_rect_height), 4)
        screen.blit(menu_background_rect_surface, (975, 500))  
        
        if not player.hearts:
            active_fruits.clear()
            if not player.score_upload:
                save_score_to_file(player)
            # pygame.time.wait(5000)
            # running_game = False
            #draw_game_over(screen)
        else:
            draw_gameplay(screen, last_fruit_spawn, spawn_interval, current_interval, fruit_types, difficulty, active_fruits, physics, player, freezing)

        for i, button in enumerate(buttons):
            button_surface, button_rectangle = create_transparent_button(
                button['text'],
                button['position'],
                (55, 55) if button['text'] in ['D', 'C', 'L'] else (90, 55) 
                if button['text'] == "U" else (150, 55),
                button_D_color if button['text'] == "D" else button_C_color if button['text'] == "C" 
                else button_L_color if button['text'] == 'L' else button_color,
                alpha_value_visible if button['text'] in ['D', 'C'] else alpha_value_transparent,
                play_pause_font if button['text'] in ["D", "C"] else home_font if button['text'] == 'L' 
                else settings_font if button['text'] == 'U' else font
            )
            if pressed_button == i:
                button_rectangle.y += 5  

            screen.blit(button_surface, button_rectangle)

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

