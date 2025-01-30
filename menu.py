import pygame
import random

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
            
# The menu
def run_menu():
    """ the first menu """
    pygame.init()

    screen = pygame.display.set_mode((1300, 600)) #see if enought or not
    pygame.display.set_caption("Space Fruits Invaders")

    background_image = pygame.image.load("media/background/star-background.jpg") #Don't forget to change the file
    background_image =  pygame.transform.scale(background_image, (1300, 600)) # To change if screen is to small
    
    png_image = pygame.image.load("media/images/alien_eating_strawberry.png")
    original_width, original_height = png_image.get_size()
    desired_height = 600
    scaling_factor = desired_height/original_height
    new_width = int(original_width*scaling_factor)
    png_image = pygame.transform.scale(png_image, (new_width, desired_height))

    click_sound = pygame.mixer.Sound("media/sounds/old-radio-button-click.mp3") # Change for the right one

    button_color = (0, 128 , 0)
    button_hover = (0, 255, 0)
    shadow_color = (0, 100, 0)

    font = pygame.font.Font(None, 36) # Change for the rigth font
    title_font = pygame.font.Font("media/font/BTTF.ttf", 45)
    large_font = pygame.font.Font("media/font/BTTF.ttf", 80)
   
    running = True
    buttons = [
        {"text":"PLAY", "position" : (65, 185)},
        {"text":"RANKING", "position" : (65, 265)},
        {"text": "SETTINGS", "position" : (65, 345)},
        {"text": "QUIT", "position" : (65, 425)},
    ]
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    button_rectangle = draw_button(screen, button ['text'], button ['position'], (150, 50), button_color, button_hover, shadow_color, font )
                    if button_rectangle.collidepoint(event.pos):
                        click_sound.play() 
                        if button['text'] == "QUIT":
                            running = False
        screen.blit(background_image, (0, 0))
        
        png_rectangle = png_image.get_rect(right = 1300, top = 0)
        screen.blit(png_image, png_rectangle)
        mouse_position = pygame.mouse.get_pos()
        if png_rectangle.collidepoint(mouse_position):
            shake_offset = random.randint(-5, 5)
            screen.blit(png_image,(png_rectangle.x + shake_offset, png_rectangle.y))
        else:
            screen.blit(png_image, png_rectangle)

        text_lines = ["Welcome &", "SPACE FRUITS", " < INVADERS!!!"]
        draw_glitched_title(screen, text_lines, "<", large_font, (240, 55), title_font)

        for button in buttons:
            draw_button(screen, button ['text'], button ['position'], (150, 50), button_color, button_hover, shadow_color, font )

        pygame.display.flip()
    
    pygame.quit()