import pygame
from utils import draw_glitched_title, create_transparent_button
import random
import sys


pygame.init()

def draw_dropdown(screen, selected_language, dropdown_open, confirmed_language):

    # Define colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    LIGHT_GRAY = (220, 220, 220)

    # Load fonts
    default_font = pygame.font.Font("media/font/Conthrax.otf", 20) 
    arrow_font = pygame.font.Font("media/font/Other_space.ttf", 30)

    # List of languages
    languages = ["English", "French"]
    confirmed_language = ""

    # Draw placeholder text
    placeholder_surface = default_font.render("Select Language:", True, WHITE)
    screen.blit(placeholder_surface, (20, 20))

    # Draw dropdown box
    dropdown_rect = pygame.Rect(20, 60, 200, 30)
    pygame.draw.rect(screen, WHITE, dropdown_rect)
    pygame.draw.rect(screen, WHITE, dropdown_rect, 2)

    # Display the selected language inside the dropdown
    display_language = selected_language if selected_language != "Select Language" else ""
    language_surface = default_font.render(display_language, True, WHITE)
    screen.blit(language_surface, (25, 65))

    # Draw arrow with border
    #arrow_rect = pygame.Rect(220, 60, 30, 30)
    #pygame.draw.rect(screen, BLACK, arrow_rect, 2)  # Draw border around the arrow
    arrow_surface = arrow_font.render("b", True, WHITE)  # Render the arrow with a specific font
    screen.blit(arrow_surface, (225, 60))  # Adjust position to center the arrow

    if dropdown_open:
        for index, lang in enumerate(languages):
            lang_rect = pygame.Rect(25, 100 + index * 30, 200, 30)
            # Change background color on hover
            if lang_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, LIGHT_GRAY, lang_rect)
            else:
                pygame.draw.rect(screen, WHITE, lang_rect)
            lang_surface = default_font.render(lang, True, BLACK)
            screen.blit(lang_surface, (30, 100 + index * 30))

    # Draw the enter button
    button_rect = pygame.Rect(255, 60, 100, 30)
    pygame.draw.rect(screen, WHITE, button_rect)
    pygame.draw.rect(screen, BLACK, button_rect, 2)
    button_surface = default_font.render("Enter", True, BLACK)
    screen.blit(button_surface, (270, 62))

    # Display selected language message if a language has been confirmed
    if confirmed_language:
        message_surface = default_font.render(f"You selected: {confirmed_language}", True, WHITE)
        screen.blit(message_surface, (20, 140))
    #screen.blit(score_surface, (50, 50))
    return selected_language, dropdown_open, confirmed_language  # Return current states

def draw_settings():
    """ The settings screen """
    screen = pygame.display.set_mode((1350, 700))
    pygame.display.set_caption("Space Fruits Invaders - Settings")

    background_image = pygame.image.load("media/background/star-background.jpg")
    background_image = pygame.transform.scale(background_image, (1350, 700)) 

    png_image = pygame.image.load("media/images/winner.png") 
    original_width, original_height = png_image.get_size()
    desired_width = 600
    scaling_factor = desired_width / original_height
    new_height = int(original_width * scaling_factor)
    png_image = pygame.transform.scale(png_image, (new_height, desired_width))

    click_sound = pygame.mixer.Sound("media/sounds/old-radio-button-click.mp3")

    font = pygame.font.Font("media/font/Conthrax.otf", 20)
    title_font = pygame.font.Font("media/font/BTTF.ttf", 45)
    large_font = pygame.font.Font("media/font/BTTF.ttf", 60)
    play_pause_font = pygame.font.Font("media/font/icons.ttf", 30)
    home_font = pygame.font.Font("media/font/alienato.TTF", 55)
    settings_font = pygame.font.Font("media/font/Other_Space.ttf", 55)

    button_color = (0, 0, 0)  
    alpha_value_transparent = 0 
    alpha_value_visible = 100  
    button_D_color = (0, 255, 0)    
    button_L_color = (0, 0, 0)

    buttons = [
        {"text": "D", "position": (1085, 620)},
        {"text": "L", "position": (1165, 620)},
        {"text": "U", "position": (1235, 620)}, 
    ]
    
    running = True
    pressed_button = None  

    # Dropdown state variables
    selected_language = "Select Language"
    dropdown_open = False
    confirmed_language = ""
    languages = ["English", "French"]

    while running:
        screen.fill((0, 0, 0))  # Fill the screen with a color
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                
                # Check if the arrow is clicked to open the dropdown
                arrow_rect = pygame.Rect(220, 60, 30, 30)
                if arrow_rect.collidepoint(mouse_pos):
                    dropdown_open = not dropdown_open
                    if dropdown_open:
                        confirmed_language = ""  # Clear the message when opening dropdown
                
                # Check if a language was selected from the dropdown
                if dropdown_open:
                    for index, lang in enumerate(languages):
                        lang_rect = pygame.Rect(25, 100 + index * 30, 200, 30)
                        if lang_rect.collidepoint(mouse_pos):
                            selected_language = lang  # Update selected language
                            dropdown_open = False  # Collapse the dropdown immediately
                
                # Check if the enter button is clicked
                button_rect = pygame.Rect(240, 60, 100, 30)
                if button_rect.collidepoint(mouse_pos):
                    if selected_language != "Select Language":
                        confirmed_language = selected_language  # Validate the choice
                        selected_language = "Select Language"  # Reset placeholder

                # Button handling
                for i, button in enumerate(buttons):
                    button_surface, button_rectangle = create_transparent_button(
                        button['text'],
                        button['position'],
                        (55, 55) if button['text'] in ['D', 'L'] else (90, 55),
                        button_D_color if button['text'] == "D" 
                        else button_L_color if button['text'] == 'L' else button_color,
                        alpha_value_visible if button['text'] == 'D' else alpha_value_transparent, 
                        play_pause_font if button['text'] == "D" else home_font if button['text'] == 'L' 
                        else settings_font if button['text'] == 'U' else font
                    )
                    if button_rectangle.collidepoint(event.pos):
                        click_sound.play() 
                        #if button['text'] == "L":            
            
                            #return   
                        #elif button["text"] == "D":
                            #gameplay_select_level()
                        #elif button["text"] == "U":
                            #function
                        pressed_button = i        
                        break

            if event.type == pygame.MOUSEBUTTONUP:
                pressed_button = None  

        screen.blit(background_image, (0, 0)) 
        
        png_rectangle = png_image.get_rect(right=1350, top=150)
        screen.blit(png_image, png_rectangle)
        mouse_position = pygame.mouse.get_pos()
        if png_rectangle.collidepoint(mouse_position):
            shake_offset = random.randint(-5, 5)
            screen.blit(png_image, (png_rectangle.x + shake_offset, png_rectangle.y))
        else:
            screen.blit(png_image, png_rectangle)

        text_lines = ["Settings"]
        draw_glitched_title(screen, text_lines, "S", large_font, (925, 40), title_font)

        menu_background_rect_width = 295
        menu_background_rect_height = 100
        menu_background_rect_surface = pygame.Surface((menu_background_rect_width, 
                                                       menu_background_rect_height), pygame.SRCALPHA) 
        black_color = (0, 0, 0, 128)  
        menu_background_rect_surface.fill(black_color)
        border_color = (255, 255, 255) 
        pygame.draw.rect(menu_background_rect_surface, border_color, (0, 0, menu_background_rect_width, 
                                                                      menu_background_rect_height), 4)
        screen.blit(menu_background_rect_surface, (1055, 600))  
        
        draw_dropdown(screen,selected_language, dropdown_open,confirmed_language)

        for i, button in enumerate(buttons):
            button_surface, button_rectangle = create_transparent_button(
                button['text'],
                button['position'],
                (55, 55) if button['text'] in ['D', 'L'] else (90, 55),
                button_D_color if button['text'] == "D" 
                else button_L_color if button['text'] == 'L' else button_color,
                alpha_value_visible if button['text'] == 'D' else alpha_value_transparent, 
                play_pause_font if button['text'] == "D" else home_font if button['text'] == 'L' 
                else settings_font if button['text'] == 'U' else font
            )
            if pressed_button == i:
                button_rectangle.y += 5  

            screen.blit(button_surface, button_rectangle)

        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    draw_settings()