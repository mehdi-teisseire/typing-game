import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Language Selection")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_GRAY = (220, 220, 220)

# Load fonts
default_font = pygame.font.Font("media/font/Conthrax.otf", 20) 
arrow_font = pygame.font.Font("media/font/Other_space.ttf", 30)

# List of languages
languages = ["English", "French"]
selected_language = "Select Language"
dropdown_open = False
confirmed_language = ""

# Function to draw the dropdown menu
def draw_dropdown(selected_language, dropdown_open):
    # Draw placeholder text
    placeholder_surface = default_font.render("Select Language:", True, BLACK)
    screen.blit(placeholder_surface, (20, 20))

    # Draw dropdown box
    dropdown_rect = pygame.Rect(20, 60, 200, 30)
    pygame.draw.rect(screen, WHITE, dropdown_rect)
    pygame.draw.rect(screen, BLACK, dropdown_rect, 2)

    # Display the selected language inside the dropdown
    display_language = selected_language if selected_language != "Select Language" else ""
    language_surface = default_font.render(display_language, True, BLACK)
    screen.blit(language_surface, (25, 65))

    # Draw arrow with border
    #arrow_rect = pygame.Rect(220, 60, 30, 30)
    #pygame.draw.rect(screen, BLACK, arrow_rect, 2)  # Draw border around the arrow
    arrow_surface = arrow_font.render("b", True, BLACK)  # Render the arrow with a specific font
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
        message_surface = default_font.render(f"You selected: {confirmed_language}", True, BLACK)
        screen.blit(message_surface, (20, 140))

# Main loop
while True:
    screen.fill(WHITE)

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

    draw_dropdown(selected_language, dropdown_open)

    pygame.display.flip()

#===============================================
import pygame
import sys

# Initialize Pygame
pygame.init()

# Function to draw the dropdown menu
def draw_dropdown(selected_language, dropdown_open, confirmed_language):
    # Set up display
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Language Selection")

    # Define colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (200, 200, 200)
    LIGHT_GRAY = (220, 220, 220)

    # Load fonts
    default_font = pygame.font.Font("media/font/Conthrax.otf", 20) 
    arrow_font = pygame.font.Font("media/font/Other_space.ttf", 30)

    # List of languages
    languages = ["English", "French"]

    # Draw placeholder text
    placeholder_surface = default_font.render("Select Language:", True, BLACK)
    screen.blit(placeholder_surface, (20, 20))

    # Draw dropdown box
    dropdown_rect = pygame.Rect(20, 60, 200, 30)
    pygame.draw.rect(screen, WHITE, dropdown_rect)
    pygame.draw.rect(screen, BLACK, dropdown_rect, 2)

    # Display the selected language inside the dropdown
    display_language = selected_language if selected_language != "Select Language" else ""
    language_surface = default_font.render(display_language, True, BLACK)
    screen.blit(language_surface, (25, 65))

    # Draw arrow with border
    arrow_surface = arrow_font.render("▼", True, BLACK)  # Render the arrow with a specific font
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
        message_surface = default_font.render(f"You selected: {confirmed_language}", True, BLACK)
        screen.blit(message_surface, (20, 140))

    return selected_language, dropdown_open, confirmed_language  # Return the current states

# Main loop
selected_language = "Select Language"
dropdown_open = False
confirmed_language = ""

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            
            # Check if the arrow is clicked to open/close the dropdown
            arrow_rect = pygame.Rect(220, 60, 30, 30)
            if arrow_rect.collidepoint(mouse_pos):
                dropdown_open = not dropdown_open
                if dropdown_open:
                    confirmed_language = ""  # Clear the message when opening dropdown
            
            # If dropdown is open, check for language selection
            if dropdown_open:
                for index, lang in enumerate(languages):
                    lang_rect = pygame.Rect(25, 100 + index * 30, 200, 30)
                    if lang_rect.collidepoint(mouse_pos):
                        selected_language = lang  # Update selected language
                        dropdown_open = False  # Collapse the dropdown immediately
            
            # Check if the enter button is clicked
            button_rect = pygame.Rect(255, 60, 100, 30)
            if button_rect.collidepoint(mouse_pos):
                if selected_language != "Select Language":
                    confirmed_language = selected_language  # Validate the choice
                    selected_language = "Select Language"  # Reset placeholder

    # Draw the dropdown menu
    selected_language, dropdown_open, confirmed_language = draw_dropdown(selected_language, dropdown_open, confirmed_language)

    pygame.display.flip()
