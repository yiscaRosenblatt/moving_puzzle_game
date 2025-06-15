import pygame
import time
from settings import *

class TopBar:
    def __init__(self, screen, font_size=36):
        self.screen = screen
        self.height = 60
        self.font = pygame.font.SysFont("timesnewroman", font_size)
        self.start_time = time.time()
        self.paused = False
        self.pause_start = None
        self.total_paused_time = 0

        self.menu_button_rect = pygame.Rect(20, 10, 120, 40)
        self.pause_button_rect = pygame.Rect(160, 10, 120, 40)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.menu_button_rect.collidepoint(event.pos):
                return "menu"
            elif self.pause_button_rect.collidepoint(event.pos):
                self.toggle_pause()
        return None

    def toggle_pause(self):
        if self.paused:
            self.total_paused_time += time.time() - self.pause_start
            self.paused = False
        else:
            self.pause_start = time.time()
            self.paused = True

    def get_elapsed_time(self):
        if self.paused:
            return int(self.pause_start - self.start_time - self.total_paused_time)
        return int(time.time() - self.start_time - self.total_paused_time)

    def draw(self):
        bar_rect = pygame.Rect(0, 0, WINDOW_WIDTH, self.height)
        pygame.draw.rect(self.screen, (230, 230, 230), bar_rect)

        pygame.draw.rect(self.screen, (139, 69, 19), self.menu_button_rect, border_radius=8)
        menu_text = self.font.render("Menu", True, WHITE)
        self.screen.blit(menu_text, menu_text.get_rect(center=self.menu_button_rect.center))

        pygame.draw.rect(self.screen, (100, 100, 100), self.pause_button_rect, border_radius=8)
        pause_label = "Resume" if self.paused else "Pause"
        pause_text = self.font.render(pause_label, True, WHITE)
        self.screen.blit(pause_text, pause_text.get_rect(center=self.pause_button_rect.center))

        time_elapsed = self.get_elapsed_time()
        minutes = time_elapsed // 60
        seconds = time_elapsed % 60
        formatted_time = f"{minutes:02}:{seconds:02}"
        timer_text = self.font.render(f"Time: {formatted_time}", True, BLACK)

        self.screen.blit(timer_text, (WINDOW_WIDTH - 180, 18))
