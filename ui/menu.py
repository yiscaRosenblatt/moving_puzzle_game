import pygame
import sys
from settings import *
from game.game import run_game

def run_menu():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Moving Puzzle Game")
    clock = pygame.time.Clock()

    # צבעים
    BACKGROUND_COLOR = (255, 255, 255)
    TEXT_COLOR = (0, 0, 0)
    BUTTON_COLOR = (139, 69, 19)
    HOVER_COLOR = (205, 133, 63)
    BUTTON_BORDER = (100, 50, 20)
    BUTTON_TEXT = (255, 255, 255)

    font = pygame.font.SysFont("timesnewroman", 60, bold=False)
    title_font = pygame.font.SysFont("timesnewroman", 60, bold=False)

    title = title_font.render("Moving Puzzle Game", True, TEXT_COLOR)
    title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, 100))

    options = [("Easy", 3), ("Medium", 4), ("Hard", 5)]
    button_width = 300
    button_height = 80

    buttons = []
    for i, (label, size) in enumerate(options):
        text = font.render(label, True, BUTTON_TEXT)
        rect = pygame.Rect(0, 0, button_width, button_height)
        rect.center = (WINDOW_WIDTH // 2, 240 + i * 100)
        text_rect = text.get_rect(center=rect.center)
        buttons.append((text, text_rect, rect, size))

    while True:
        screen.fill(BACKGROUND_COLOR)
        screen.blit(title, title_rect)

        mouse_pos = pygame.mouse.get_pos()
        hovering = False

        for text, text_rect, rect, _ in buttons:
            if rect.collidepoint(mouse_pos):
                button_color = HOVER_COLOR
                hovering = True
            else:
                button_color = BUTTON_COLOR

            pygame.draw.rect(screen, button_color, rect, border_radius=10)
            pygame.draw.rect(screen, BUTTON_BORDER, rect, 3, border_radius=10)
            screen.blit(text, text_rect)

        if hovering:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                for _, _, rect, size in buttons:
                    if rect.collidepoint(event.pos):
                        run_game(screen, clock, size)

        pygame.display.flip()
        clock.tick(60)
