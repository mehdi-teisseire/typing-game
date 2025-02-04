import pygame
import sys
import random

def draw_dropdown(screen, selected_language, dropdown_open, confirmed_language):
    """ The language dropdown menu """
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    LIGHT_GRAY = (220, 220, 220)
    default_font = pygame.font.Font("media/font/Conthrax.otf", 20)
    arrow_font = pygame.font.Font("media/font/Other_space.ttf", 30)

    languages = ["English", "French"]
    
    pygame.display.set_caption("Language Selection")

    popup_width, popup_height = 400, 300
    popup_x = (screen.get_width() - popup_width) // 2
    popup_y = (screen.get_height() - popup_height) // 2

    pygame.draw.rect(screen, (0, 0, 0), (popup_x, popup_y, popup_width, popup_height)) 
    pygame.draw.rect(screen, (255, 255, 255), (popup_x, popup_y, popup_width, popup_height), 4) 

    placeholder_surface = default_font.render("Select Language:", True, WHITE)
    screen.blit(placeholder_surface, (500, 225))

    dropdown_rect = pygame.Rect(500, 260, 200, 40)
    pygame.draw.rect(screen, WHITE, dropdown_rect)
    pygame.draw.rect(screen, WHITE, dropdown_rect, 2)

    display_language = selected_language if selected_language != "Select Language" else ""
    language_surface = default_font.render(display_language, True, BLACK)
    screen.blit(language_surface, (510, 267))

    arrow_surface = arrow_font.render("b", True, WHITE)  
    screen.blit(arrow_surface, (705, 260)) 

    if dropdown_open:
        for index, lang in enumerate(languages):
            lang_rect = pygame.Rect(500, 300 + index * 30, 200, 30)
            pygame.draw.rect(screen, LIGHT_GRAY if lang_rect.collidepoint(pygame.mouse.get_pos()) else WHITE, lang_rect)
            lang_surface = default_font.render(lang, True, BLACK)
            screen.blit(lang_surface, (505, 300 + index * 30))

    button_rect = pygame.Rect(740, 260, 95, 40)
    pygame.draw.rect(screen, WHITE, button_rect)
    pygame.draw.rect(screen, WHITE, button_rect, 2)
    button_surface = default_font.render("Enter", True, BLACK)
    screen.blit(button_surface, (750, 267))

    if confirmed_language:
        message_surface = default_font.render(f"You selected: {confirmed_language}", True, WHITE)
        screen.blit(message_surface, (500, 350))

    back_button_rect = pygame.Rect(625, 445, 110, 40)
    pygame.draw.rect(screen, WHITE, back_button_rect)
    pygame.draw.rect(screen, WHITE, back_button_rect, 2)
    back_button_surface = default_font.render("CLOSE", True, BLACK)
    screen.blit(back_button_surface, (635, 452))

def create_flying_letters(font, flying_color, size, screen_width, screen_height):
    letters = []
    for _ in range(20):  
        letter = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')  
        x = random.randint(0, screen_width)
        y = random.randint(-100, screen_height)  
        speed = random.uniform(0, 1) 
        letters.append({'letter': letter, 'x': x, 'y': y, 'speed': speed, 'font' :font,
                         'flying_color': flying_color, 'size': size})
    return letters

def update_flying_letters(letters):
    for letter in letters:
        letter['y'] += letter['speed'] 
        if letter['y'] > 700: 
            letter['y'] = random.randint(-100, -10)
            letter['x'] = random.randint(0, 1350)
            letter['letter'] = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

def draw_flying_letters(screen, letters, font, color):
    for letter in letters:
        letter_surface = font.render(letter['letter'], True, color)
        screen.blit(letter_surface, (letter['x'], letter['y']))

def language():
    pygame.init()
    screen = pygame.display.set_mode((1350, 700))
    background_image = pygame.image.load('media/background/star-background.jpg') 
    background_image = pygame.transform.scale(background_image, (1350, 700))  
    selected_language = "Select Language"
    dropdown_open = False
    confirmed_language = ""
    popup_open = True

    flying_font = pygame.font.Font("media/font/alienato.ttf", 90) 
    flying_color = (0, 220, 0)  
    flying_letters = create_flying_letters(flying_font, flying_color, 30, 1350, 700)

    while popup_open:
        screen.blit(background_image, (0, 0))
        update_flying_letters(flying_letters)
        draw_flying_letters(screen, flying_letters, flying_font, flying_color)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                
                arrow_rect = pygame.Rect(705, 260, 30, 30)
                if arrow_rect.collidepoint(mouse_pos):
                    dropdown_open = not dropdown_open
                    if dropdown_open:
                        confirmed_language = ""  
                
                if dropdown_open:
                    for index, lang in enumerate(["English", "French"]):
                        lang_rect = pygame.Rect(500, 300 + index * 30, 200, 30)
                        if lang_rect.collidepoint(mouse_pos):
                            selected_language = lang  
                            dropdown_open = False 
                
                button_rect = pygame.Rect(740, 260, 100, 40)
                if button_rect.collidepoint(mouse_pos):
                    if selected_language != "Select Language":
                        confirmed_language = selected_language  
                        selected_language = "Select Language"  
                
                back_button_rect = pygame.Rect(625, 450, 80, 40)
                if back_button_rect.collidepoint(mouse_pos):
                    popup_open = False

        draw_dropdown(screen, selected_language, dropdown_open, confirmed_language)
        pygame.display.flip()

if __name__ == "__main__":
    language()