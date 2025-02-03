import pygame
from utils import draw_glitched_title, create_transparent_button
import random
import sys

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

# To sort scores in descending order
def sort_scores(scores):
    return sorted(scores, key=lambda x: x['score'], reverse=True) 

# To draw the score screen
def draw_score_screen(screen, scores, offset_y):
    font = pygame.font.Font("media/font/Conthrax.otf", 36)
    title_text = font.render("BEST PLAYERS", True, (255, 255, 255))
    screen.blit(title_text, (225, 50))

    font = pygame.font.Font("media/font/Conthrax.otf", 20)
    y_offset = 150 - offset_y

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

# Area to display the score 
def score_area(screen, scores, scroll_offset):
    """ The score area """
    score_surface = pygame.Surface((800, 600))
    score_surface = pygame.image.load("media/background/star-background.jpg")
    score_surface = pygame.transform.scale(score_surface, (800, 600))
    border_color = (255, 255, 255) 
    pygame.draw.rect(score_surface, border_color, (0, 0, 800, 600), 4) 

    draw_score_screen(score_surface, scores, scroll_offset)

    screen.blit(score_surface, (50, 50))

    scrollbar_height = 250
    scrollbar_width = 10
    scrollbar_x = screen.get_width() - scrollbar_width - 480
    max_scroll_offset = max(0, len(scores) * 30 - 400)
    scrollbar_y = 150 + (scroll_offset / max_scroll_offset * scrollbar_height) if max_scroll_offset > 0 else 150
    pygame.draw.rect(screen, (255, 255, 255), (scrollbar_x, scrollbar_y, scrollbar_width, scrollbar_height))

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

    title_font = pygame.font.Font("media/font/BTTF.ttf", 45)
    large_font = pygame.font.Font("media/font/BTTF.ttf", 60)
    settings_font = pygame.font.Font("media/font/Other_Space.ttf", 55)

    scroll_offset = 0
    is_scrolling = False
    scroll_start_y = 0

    alpha_value_transparent = 0 
    button_U_color = (0, 0, 0)

    buttons = [
        {"text": "U", "position": (1235, 620)},  
    ]
    
    running = True
    pressed_button = None  

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if event.button == 1:  
                    scrollbar_x = screen.get_width() - 490 
                    scrollbar_y = 150 + (scroll_offset / max(1, len(sorted_scores) * 30 - 400))
                    if scrollbar_x <= mouse_pos[0] <= scrollbar_x + 10 and scrollbar_y <= mouse_pos[1] <= scrollbar_y + 400:
                        is_scrolling = True
                        scroll_start_y = mouse_pos[1]
            if event.type == pygame.MOUSEMOTION and is_scrolling:
                delta_y = event.pos[1] - scroll_start_y
                scroll_offset += int(delta_y * (len(sorted_scores) / 25)) 
                max_scroll_offset = max(0, len(sorted_scores) * 30 - 400)
                scroll_offset = max(0, min(scroll_offset, max_scroll_offset))  
                scroll_start_y = event.pos[1] 
            if event.type == pygame.MOUSEBUTTONUP:
                is_scrolling = False

            screen.blit(background_image, (0, 0))

            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, button in enumerate(buttons):
                    mouse_pos = event.pos
                    button_surface, button_rectangle = create_transparent_button(
                        button['text'],
                        button['position'],
                        (90, 55),  
                        button_U_color,
                        alpha_value_transparent,
                        settings_font
                    )
                    if button_rectangle.collidepoint(mouse_pos):
                        click_sound.play() 
                        if button['text'] == 'U':
                            running = False

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

        menu_background_rect_width = 130
        menu_background_rect_height = 100
        menu_background_rect_surface = pygame.Surface((menu_background_rect_width, menu_background_rect_height), pygame.SRCALPHA) 
        black_color = (0, 0, 0, 128)  
        menu_background_rect_surface.fill(black_color)
        border_color = (255, 255, 255) 
        pygame.draw.rect(menu_background_rect_surface, border_color, (0, 0, menu_background_rect_width, menu_background_rect_height), 4)
        screen.blit(menu_background_rect_surface, (1220, 600))  
        
        score_area(screen, sorted_scores, scroll_offset)

        for i, button in enumerate(buttons):
            button_surface, button_rectangle = create_transparent_button(
                button['text'],
                button['position'],
                (90, 55),
                button_U_color,
                alpha_value_transparent,
                settings_font
            )
            if pressed_button == i:
                button_rectangle.y += 5  

            screen.blit(button_surface, button_rectangle)

        pygame.display.flip()
    

if __name__ == "__main__":
    draw_score()