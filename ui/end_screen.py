import pygame
from settings import *

class EndScreen:
    def __init__(self, screen, elapsed_time):
        self.screen = screen
        self.elapsed_time = elapsed_time
        self.font_big = pygame.font.SysFont("timesnewroman", 64)
        self.font_small = pygame.font.SysFont("timesnewroman", 40)

        self.button_again = pygame.Rect(WINDOW_WIDTH // 2 - 140, 300, 280, 60)
        self.button_menu = pygame.Rect(WINDOW_WIDTH // 2 - 140, 380, 280, 60)

    def draw_blurred_overlay(self):
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        self.screen.blit(overlay, (0, 0))

    def draw(self):
        self.draw_blurred_overlay()

        title_text = self.font_big.render("Well Done!", True, WHITE)
        self.screen.blit(title_text, title_text.get_rect(center=(WINDOW_WIDTH // 2, 120)))

        time_text = self.font_small.render(f"You finished in {self.elapsed_time} seconds!", True, WHITE)
        self.screen.blit(time_text, time_text.get_rect(center=(WINDOW_WIDTH // 2, 200)))

        pygame.draw.rect(self.screen, (139, 69, 19), self.button_again, border_radius=10)
        again_text = self.font_small.render("Play Again", True, WHITE)
        self.screen.blit(again_text, again_text.get_rect(center=self.button_again.center))

        pygame.draw.rect(self.screen, (100, 100, 100), self.button_menu, border_radius=10)
        menu_text = self.font_small.render("Back to Menu", True, WHITE)
        self.screen.blit(menu_text, menu_text.get_rect(center=self.button_menu.center))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_again.collidepoint(event.pos):
                return "again"
            elif self.button_menu.collidepoint(event.pos):
                return "menu"
        return None
