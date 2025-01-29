import pygame
pygame.init()

# To draw buttons
def draw_button(screen, text, position, size, color, hover_color, shadow_color, font, pulse_rate = 1.1):
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
