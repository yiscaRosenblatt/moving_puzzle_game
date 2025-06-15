import sys
import pygame
from logic.board import Board
from settings import BLACK
from ui.topbar import TopBar
from ui.end_screen import EndScreen

def format_time(seconds):
    minutes = seconds // 60
    sec = seconds % 60
    return f"{minutes:02}:{sec:02}"

def run_game(screen, clock, board_size):
    topbar = TopBar(screen)
    board = Board(board_size)

    game_over = False
    end_screen = None

    while True:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if game_over:
                action = end_screen.handle_event(event)
                if action == "menu":
                    return
                elif action == "again":
                    return run_game(screen, clock, board_size)
            else:
                action = topbar.handle_event(event)
                if action == "menu":
                    return
                if not topbar.paused:
                    board.handle_event(event)

        if not game_over and not topbar.paused:
            board.update()
            if board.is_solved():
                game_over = True
                elapsed = topbar.get_elapsed_time()
                end_screen = EndScreen(screen, format_time(elapsed))

        board.draw(screen)
        topbar.draw()

        if game_over:
            end_screen.draw()

        pygame.display.flip()
        clock.tick(60)
