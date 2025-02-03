import pygame
import random

from score import draw_score
from utils import draw_button, draw_glitched_title



pygame.init()

# To draw buttons
def draw_button(screen, text, position, size, color, hover_color, shadow_color, font, pulse_rate = 1.1):
    """ to draw buttons """
    x, y = position
    width, height = size
    button_rect = pygame.Rect (x, y, width, height)

    shadow_rect =button_rect.move(5,5)
    pygame.draw.rect(screen, shadow_color, shadow_rect)

    mouse_position = pygame.mouse.get_pos()
    if button_rect.collidepoint (mouse_position):
        pygame.draw.rect(screen, hover_color, button_rect.inflate(int(width*(pulse_rate - 1)), int(height*(pulse_rate -1))))
    
    else :
        pygame.draw.rect(screen, color, button_rect)
    
    text_surface = font.render(text, True, (255, 255, 255)) # Change color depending on the background
    text_rect = text_surface.get_rect(center = button_rect.center)
    screen.blit(text_surface, text_rect)

    return button_rect
        
#Make the arrow bigger and glitch the text
def draw_glitched_title(screen, text_lines, larger_character, large_font, position, title_font):
    """ Draw lines of text with a specific character larger, a glicht effect and rotate """
    line_height = title_font.get_linesize()

    for index, line in enumerate(text_lines):
        x_offset = position [0]
        y_position = position [1] + index*line_height

        for _ in range(random.randint(1,3)):
            x_offset = position[0]
            y_position_offset = y_position + random.randint(-2,2)

            for character in line:
                if character == larger_character:
                    text_surface = large_font.render(character, True, (255, 255, 255))
                    screen.blit(text_surface,(x_offset, y_position_offset))
                    x_offset  += text_surface.get_width()
                else:
                    text_surface = title_font.render(character, True, (255, 255, 255))
                    screen.blit(text_surface,(x_offset,y_position_offset))
                    x_offset += text_surface.get_width()



    screen = pygame.display.set_mode((1350, 700))
    pygame.display.set_caption("Space Fruits Invaders")

    background_image = pygame.image.load("media/background/star-background.jpg") 
    background_image =  pygame.transform.scale(background_image, (1350, 700)) 
    
    png_image = pygame.image.load("media/images/alien_eating_strawberry.png")
    original_width, original_height = png_image.get_size()
    desired_height = 700
=======
    screen = pygame.display.set_mode((1300, 600)) #see if enought or not
    pygame.display.set_caption("Space Fruits Invaders")

    background_image = pygame.image.load("media/background/star-background.jpg") #Don't forget to change the file
    background_image =  pygame.transform.scale(background_image, (1300, 600)) # To change if screen is to small
    
    png_image = pygame.image.load("media/images/alien_eating_strawberry.png")
    original_width, original_height = png_image.get_size()
    desired_height = 600
 # Change for the right one

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

