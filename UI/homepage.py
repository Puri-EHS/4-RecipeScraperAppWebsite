import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Recipe Creator")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Fonts
font_large = pygame.font.Font(None, 36)
font_medium = pygame.font.Font(None, 24)

# Ingredients list
ingredients = []

# Pages
HOME_PAGE = 0
FILTER_SEARCH_PAGE = 1
current_page = HOME_PAGE

# Button dimensions
button_width, button_height = 200, 50

# Function to draw text on screen
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

# Function to draw buttons
def draw_button(text, x, y, width, height, inactive_color, active_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(screen, active_color, (x, y, width, height))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(screen, inactive_color, (x, y, width, height))

    draw_text(text, font_medium, BLACK, x + width / 2, y + height / 2)

# Function to handle button actions
def filter_search_action():
    global current_page
    current_page = FILTER_SEARCH_PAGE

def back_to_home_action():
    global current_page
    current_page = HOME_PAGE

def add_ingredient_action():
    ingredient = filter_search_page_elements[1].get_text()
    if ingredient:
        ingredients.append(ingredient)
        filter_search_page_elements[1].set_text("")

def delete_ingredient_action(index):
    del ingredients[index]

# Main Loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if current_page == HOME_PAGE:
        draw_text("Recipe Creator", font_large, BLACK, screen_width / 2, 100)
        draw_button("Filter Search", 300, 200, button_width, button_height, GRAY, BLACK, filter_search_action)
        draw_button("Recipe Search", 300, 300, button_width, button_height, GRAY, BLACK)

    elif current_page == FILTER_SEARCH_PAGE:
        draw_button("Back", 20, 20, button_width, button_height, GRAY, BLACK, back_to_home_action)
        pygame.draw.rect(screen, GRAY, (150, 20, 300, 30))
        pygame.draw.rect(screen, GRAY, (470, 20, 100, 30))
        draw_text("Add", font_medium, BLACK, 520, 35)
        draw_text("Ingredient:", font_medium, BLACK, 20, 80)

        ingredient_input = pygame.Rect(150, 50, 300, 30)
        pygame.draw.rect(screen, BLACK, ingredient_input, 2)

        filter_search_page_elements = [
            pygame.Rect(150, 120 + i * 30, 300, 30) for i, _ in enumerate(ingredients)
        ]

        for i, ingredient in enumerate(ingredients):
            draw_text(ingredient, font_medium, BLACK, 150, 120 + i * 30)
            draw_button("Delete", 500, 120 + i * 30, 100, 30, GRAY, BLACK, lambda i=i: delete_ingredient_action(i))

    pygame.display.flip()

pygame.quit()
