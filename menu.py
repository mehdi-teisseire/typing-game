import pygame
import random
from score import draw_score
from utils import draw_button, draw_glitched_title

pygame.init()

# The menu
def run_menu():
    """ the first menu """
    pygame.init()

    screen = pygame.display.set_mode((1350, 700))
    pygame.display.set_caption("Space Fruits Invaders")

    background_image = pygame.image.load("media/background/star-background.jpg") 
    background_image =  pygame.transform.scale(background_image, (1350, 700)) 
    
    png_image = pygame.image.load("media/images/alien_eating_strawberry.png")
    original_width, original_height = png_image.get_size()
    desired_height = 700
    scaling_factor = desired_height/original_height
    new_width = int(original_width*scaling_factor)
    png_image = pygame.transform.scale(png_image, (new_width, desired_height))

    click_sound = pygame.mixer.Sound("media/sounds/old-radio-button-click.mp3") # Change for the right one

    button_color = (0, 128 , 0)
    button_hover = (0, 225, 0)
    shadow_color = (0, 80, 0)

    font = pygame.font.Font("media/font/Conthrax.otf", 20) 
    title_font = pygame.font.Font("media/font/BTTF.ttf", 45)
    large_font = pygame.font.Font("media/font/BTTF.ttf", 70)
   
    running = True
    buttons = [
        {"text":"PLAY", "position" : (60, 225)},
        {"text":"RANKING", "position" : (60, 325)},
        {"text": "SETTINGS", "position" : (60, 425)},
        {"text": "QUIT", "position" : (60, 525)},
    ]
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    button_rectangle = draw_button(screen, button ['text'], 
                                                   button ['position'], (150, 50), 
                                                   button_color, button_hover, 
                                                   shadow_color, font )
                    if button_rectangle.collidepoint(event.pos):
                        click_sound.play() 
                        if button ['text'] == "PLAY":
                            gameplay_select_level()
                        if button ['text'] == "RANKING":
                            draw_score()
                        #if button ['text'] == "SETTINGS"
                            #add function for the setting page
                        if button['text'] == "QUIT":
                            running = False
        screen.blit(background_image, (0, 0))
        
        png_rectangle = png_image.get_rect(right = 1350, top = 0)
        screen.blit(png_image, png_rectangle)
        mouse_position = pygame.mouse.get_pos()
        if png_rectangle.collidepoint(mouse_position):
            shake_offset = random.randint(-5, 5)
            screen.blit(png_image,(png_rectangle.x + shake_offset, png_rectangle.y))
        else:
            screen.blit(png_image, png_rectangle)

        text_lines = ["Welcome &", "SPACE FRUITS", " < INVADERS!!!"]
        draw_glitched_title(screen, text_lines, "<", large_font, (225, 90), title_font)

        for button in buttons:
            draw_button(screen, button ['text'], button ['position'], (150, 55), 
                        button_color, button_hover, shadow_color, font )

        pygame.display.flip()
    
    pygame.quit()

from game import gameplay

def gameplay_select_level():
    current_level = "NORMAL" 

    while True: 
        selected_level = gameplay(
            f"media/background/{current_level}_background.jpg",
            f"media/images/{current_level}_alien.png",
            current_level
        )

        if selected_level in ['NORMAL', 'EASY', 'ENDLESS', 'HARD']:
            current_level = selected_level 

if __name__ == "__main__":
    gameplay_select_level()