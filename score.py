import pygame
from utils import draw_glitched_title, create_transparent_button
import random
#from menu import run_menu

pygame.init()

# To read scores from a file
def read_scores_from_file(scores):
    scores = []
    try:
        with open('scores.txt', 'r', encoding='utf-8') as file:
            for line in file:
                name, score = line.strip().split(',')
                scores.append({'name': name, 'score': int(score)})
    except FileNotFoundError:
        print("Score file not found.")
    return scores

# To sort scores in deescending order
def sort_scores(scores):
    return sorted(scores, key=lambda x: x['score'], reverse=True) 

# To draw the score screen
def draw_score_screen(screen, scores, offset_y):
    font = pygame.font.Font("media/font/Conthrax.otf", 36)
    title_text = font.render("BEST PLAYERS", True, (255, 255, 255))
    screen.blit(title_text, (100, 50))

    font = pygame.font.Font("media/font/Conthrax.otf", 20)
    y_offset = 150 + offset_y

    if not scores:
        no_scores_text = font.render("No scores available.", True, (255, 255, 255))
        screen.blit(no_scores_text, (100, y_offset))
        y_offset += 30 

    sorted_scores = sort_scores(scores)

    for index, entry in enumerate(sorted_scores):
        rank_text = font.render(str(index + 1), True, (255, 255, 255))
        name_text = font.render(entry['name'], True, (255, 255, 255))
        score_text = font.render(str(entry['score']), True, (255, 255, 255))

        screen.blit(rank_text, (50, y_offset))
        screen.blit(name_text, (100, y_offset))

        score_width = score_text.get_width()
        score_x_position = screen.get_width() - score_width - 100  
        screen.blit(score_text, (score_x_position, y_offset))

        if entry['score'] == max(score['score'] for score in scores):
            trophy_image = pygame.image.load("media/icons/star.png")
            trophy_image = pygame.transform.scale(trophy_image, (20, 20))  
            screen.blit(trophy_image, (score_x_position + 60, y_offset - 10))

        y_offset += 30 

    #scrollbar_height = 400 
    #scrollbar_width = 10
    #pygame.draw.rect(screen, (255, 255, 255), (screen.get_width() - scrollbar_width - 10, 150, scrollbar_width, scrollbar_height))  # Adjust position as needed

# Area to display the score 
def score_area (screen, scores):
    """ The score area """
    score_surface = pygame.Surface((800, 600))
    score_surface = pygame.image.load("media/background/star-background.jpg")
    score_surface = pygame.transform.scale(score_surface, (800, 600))
    border_color = (255, 255, 255) 
    pygame.draw.rect(score_surface, border_color, (0, 0, 800, 600), 4) 

    draw_score_screen(score_surface, scores, 0)

    screen.blit(score_surface, (50, 50))

# The score skin
def draw_score():
    """ The score skin """
    screen = pygame.display.set_mode((1350, 700))
    pygame.display.set_caption("Space Fruits Invaders - Best Players are?")

    background_image = pygame.image.load("media/background/star-background.jpg")
    background_image = pygame.transform.scale(background_image, (1350, 700)) 

    scores = read_scores_from_file("scores.txt")
    sorted_scores = sort_scores(scores)
    
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

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, button in enumerate(buttons):
                    button_surface, button_rectangle = create_transparent_button(
                    button['text'],
                    button['position'],
                    (55, 55) if button ['text'] in ['D', 'L'] else (90, 55),
                    button_D_color if button['text'] == "D" 
                    else button_L_color if button['text'] == 'L' else button_color,
                    alpha_value_visible if button['text'] == 'D' else alpha_value_transparent, 
                    play_pause_font if button['text'] == "D" else home_font if button['text'] == 'L' 
                    else settings_font if button['text'] == 'U' else font
                )
                    if button_rectangle.collidepoint(event.pos):
                        click_sound.play() 
 
                        #if button['text'] == "L":            
                            #run_menu()             
                            #return   
                        #elif button["text"] == "D":
                        # function
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

        text_lines = ["The Hall", "Of Fame"]
        draw_glitched_title(screen, text_lines, "H", large_font, (925, 40), title_font)

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
        
        score_area(screen, sorted_scores)

        for i, button in enumerate(buttons):
            button_surface, button_rectangle = create_transparent_button(
            button['text'],
            button['position'],
            (55, 55) if button ['text'] in ['D', 'L'] else (90, 55),
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
    draw_score()
    
