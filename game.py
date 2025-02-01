import pygame
from menu import draw_glitched_title
import random

pygame.init()

# Transparent buttons for the small player menu
def create_transparent_button(text, position, size, color, alpha, font):
    """Transparent buttons for the small player menu"""
    button_surface = pygame.Surface(size, pygame.SRCALPHA)
    button_surface.fill((0, 0, 0, 0))
    pygame.draw.rect(button_surface, color + (alpha,), (0, 0, size[0], size[1]))

    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(size[0] // 2, size[1] // 2))
    button_surface.blit(text_surface, text_rect)

    return button_surface, button_surface.get_rect(topleft=position)

# To display the gameplay
def draw_gameplay(screen):
    """ The gameplay area """
    gameplay_surface = pygame.Surface((800, 600))
    gameplay_surface = pygame.image.load("media/background/star-background.jpg")
    gameplay_surface = pygame.transform.scale(gameplay_surface, (800, 600))
    border_color = (255, 255, 255) 
    pygame.draw.rect(gameplay_surface, border_color, (0, 0, 800, 600), 4) 
    
    heart_icon = pygame.image.load("media/icons/heart.png")
    heart_icon = pygame.transform.scale(heart_icon, (25, 25))
    hearts = 3
    for index in range(hearts):
        gameplay_surface.blit(heart_icon, (10 + index * 30, 10))

    star_icon = pygame.image.load("media/icons/star.png")
    star_icon = pygame.transform.scale(star_icon, (25,25))
    gameplay_surface.blit(star_icon, (670, 10))
    score = 0
    font = pygame.font.Font("media/font/Conthrax.otf", 20)
    score_surface = font.render(f"{score}", True, (255, 255, 255))
    gameplay_surface.blit(score_surface, (700, 11))

    screen.blit(gameplay_surface, (50, 50))

# General function for the game 
def gameplay(background_path, alien_image_path, title_text):
    """General function for the game """
    screen = pygame.display.set_mode((1350, 700))
    pygame.display.set_caption(f"Space Fruits Invaders - Difficulty: {title_text}")

    background_image = pygame.image.load(background_path)
    background_image = pygame.transform.scale(background_image, (1350, 700))
   
    png_image = pygame.image.load(alien_image_path)
    original_width, original_height = png_image.get_size()
    desired_width = 400
    scaling_factor = desired_width / original_height
    new_height = int(original_width * scaling_factor)
    png_image = pygame.transform.scale(png_image, (new_height, desired_width))

    click_sound = pygame.mixer.Sound("media/sounds/old-radio-button-click.mp3")

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
   
    running = True
    pressed_button = None  
    selected_level = None  

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
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
                        pressed_button = i
                        break 

            if event.type == pygame.MOUSEBUTTONUP:
                pressed_button = None  

        screen.blit(background_image, (0, 0)) 
        
        png_rectangle = png_image.get_rect(right=1350, top=100)
        screen.blit(png_image, png_rectangle)
        mouse_position = pygame.mouse.get_pos()
        if png_rectangle.collidepoint(mouse_position):
            shake_offset = random.randint(-5, 5)
            screen.blit(png_image, (png_rectangle.x + shake_offset, png_rectangle.y))
        else:
            screen.blit(png_image, png_rectangle)

        text_lines = [title_text]  
        draw_glitched_title(screen, text_lines, title_text[0], large_font, (925, 40), title_font)

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
        
        draw_gameplay(screen)

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
    
    pygame.quit()

