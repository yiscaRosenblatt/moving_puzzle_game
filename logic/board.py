import random
import pygame
import time
from settings import *

MOVE_SOUND_PATH = "sounds/move1.wav"
WIN_SOUND_PATH = "sounds/win1.wav"

class Board:
    def __init__(self, size):
        self.size = size
        self.tiles = self.generate_solvable_board()
        self.empty_pos = self.find_empty()
        self.font = pygame.font.SysFont("timesnewroman", 72)
        self.start_time = time.time()
        self.solved = False

        pygame.mixer.init()
        self.move_sound = pygame.mixer.Sound(MOVE_SOUND_PATH)
        self.win_sound = pygame.mixer.Sound(WIN_SOUND_PATH)

        while self.is_solved():
            self.tiles = self.generate_solvable_board()
            self.empty_pos = self.find_empty()

    def generate_solvable_board(self):
        numbers = list(range(1, self.size ** 2)) + [None]
        while True:
            random.shuffle(numbers)
            if self.is_solvable(numbers):
                break
        return [numbers[i:i + self.size] for i in range(0, len(numbers), self.size)]

    def is_solved(self):
        expected = list(range(1, self.size ** 2)) + [None]
        flat_tiles = [tile for row in self.tiles for tile in row]
        return flat_tiles == expected

    def find_empty(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.tiles[row][col] is None:
                    return (row, col)

    def is_solvable(self, nums):
        inv_count = 0
        flat = [n for n in nums if n is not None]
        for i in range(len(flat)):
            for j in range(i + 1, len(flat)):
                if flat[i] > flat[j]:
                    inv_count += 1
        if self.size % 2 == 1:
            return inv_count % 2 == 0
        else:
            empty_row = nums.index(None) // self.size
            return (inv_count + empty_row) % 2 == 1

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            tile_size = WINDOW_WIDTH // self.size
            row = y // tile_size
            col = x // tile_size

            if self.is_adjacent(row, col, *self.empty_pos):
                self.tiles[self.empty_pos[0]][self.empty_pos[1]] = self.tiles[row][col]
                self.tiles[row][col] = None
                self.empty_pos = (row, col)
                self.move_sound.play()

    def is_adjacent(self, r1, c1, r2, c2):
        return (abs(r1 - r2) == 1 and c1 == c2) or (abs(c1 - c2) == 1 and r1 == r2)

    def update(self):
        if self.is_solved() and not self.solved:
            self.win_sound.play()
            self.solved = True

    def draw(self, screen):
        tile_size = WINDOW_WIDTH // self.size
        offset_y = 60

        for row in range(self.size):
            for col in range(self.size):
                value = self.tiles[row][col]
                rect = pygame.Rect(
                    col * tile_size,
                    row * tile_size + offset_y,
                    tile_size,
                    tile_size
                )
                if value is None:
                    pygame.draw.rect(screen, EMPTY_TILE_COLOR, rect)
                else:
                    pygame.draw.rect(screen, TILE_COLOR, rect)
                    text = self.font.render(str(value), True, WHITE)
                    text_rect = text.get_rect(center=rect.center)
                    screen.blit(text, text_rect)

                pygame.draw.rect(screen, WHITE, rect, 2)



