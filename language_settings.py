import pygame
import sys

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

    pygame.draw.rect(screen, (200, 200, 200), (popup_x, popup_y, popup_width, popup_height))  # Gray background
    pygame.draw.rect(screen, (0, 0, 0), (popup_x, popup_y, popup_width, popup_height), 2)  # Black border

    placeholder_surface = default_font.render("Select Language:", True, BLACK)
    screen.blit(placeholder_surface, (20, 20))

    dropdown_rect = pygame.Rect(20, 60, 200, 30)
    pygame.draw.rect(screen, WHITE, dropdown_rect)
    pygame.draw.rect(screen, BLACK, dropdown_rect, 2)

    display_language = selected_language if selected_language != "Select Language" else ""
    language_surface = default_font.render(display_language, True, BLACK)
    screen.blit(language_surface, (25, 65))

    arrow_surface = arrow_font.render("b", True, BLACK)  
    screen.blit(arrow_surface, (225, 60)) 

    if dropdown_open:
        for index, lang in enumerate(languages):
            lang_rect = pygame.Rect(25, 100 + index * 30, 200, 30)
            pygame.draw.rect(screen, LIGHT_GRAY if lang_rect.collidepoint(pygame.mouse.get_pos()) else WHITE, lang_rect)
            lang_surface = default_font.render(lang, True, BLACK)
            screen.blit(lang_surface, (30, 100 + index * 30))

    button_rect = pygame.Rect(255, 60, 100, 30)
    pygame.draw.rect(screen, WHITE, button_rect)
    pygame.draw.rect(screen, BLACK, button_rect, 2)
    button_surface = default_font.render("Enter", True, BLACK)
    screen.blit(button_surface, (270, 62))

    if confirmed_language:
        message_surface = default_font.render(f"You selected: {confirmed_language}", True, BLACK)
        screen.blit(message_surface, (20, 140))

    back_button_rect = pygame.Rect(300, 250, 80, 30)
    pygame.draw.rect(screen, WHITE, back_button_rect)
    pygame.draw.rect(screen, BLACK, back_button_rect, 2)
    back_button_surface = default_font.render("Back", True, BLACK)
    screen.blit(back_button_surface, (315, 252))

def language():
    pygame.init()
    screen = pygame.display.set_mode((1350, 700))
    selected_language = "Select Language"
    dropdown_open = False
    confirmed_language = ""
    popup_open = True

    while popup_open:
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                
                arrow_rect = pygame.Rect(220, 60, 30, 30)
                if arrow_rect.collidepoint(mouse_pos):
                    dropdown_open = not dropdown_open
                    if dropdown_open:
                        confirmed_language = ""  
                
                if dropdown_open:
                    for index, lang in enumerate(["English", "French"]):
                        lang_rect = pygame.Rect(25, 100 + index * 30, 200, 30)
                        if lang_rect.collidepoint(mouse_pos):
                            selected_language = lang  
                            dropdown_open = False 
                
                button_rect = pygame.Rect(240, 60, 100, 30)
                if button_rect.collidepoint(mouse_pos):
                    if selected_language != "Select Language":
                        confirmed_language = selected_language  
                        selected_language = "Select Language"  
                
                back_button_rect = pygame.Rect(300, 250, 80, 30)
                if back_button_rect.collidepoint(mouse_pos):
                    popup_open = False


        draw_dropdown(screen, selected_language, dropdown_open, confirmed_language)
        pygame.display.flip()

if __name__ == "__main__":
    language()