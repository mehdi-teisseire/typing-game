import pygame
import random

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
    
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center = button_rect.center)
    screen.blit(text_surface, text_rect)

    return button_rect

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

#Make the arrow bigger and glitch the text
def draw_glitched_title(screen, text_lines, larger_character, large_font, position, title_font):
    """ Draw lines of text with a specific character larger, a glitch effect """
    line_height = title_font.get_linesize()

    for index, line in enumerate(text_lines):
        x_offset = position [0]
        y_position = position [1] + index*1.2*line_height

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

