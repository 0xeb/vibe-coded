import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_SIZE = 600
CELL_SIZE = SCREEN_SIZE // 3
BACKGROUND_COLOR = (255, 255, 255)  # White
LINE_COLOR = (0, 0, 0)             # Black
X_COLOR = (0, 0, 255)              # Blue
O_COLOR = (255, 0, 0)              # Red
LINE_WIDTH = 2
SYMBOL_WIDTH = 3
SYMBOL_MARGIN = 50
FONT_SIZE = 40

# Create game window
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Tic Tac Toe")

class Board:
    def __init__(self):
        self.reset_game()
    
    def reset_game(self):
        # Initialize empty 3x3 board
        self.grid = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.winner = None
        self.game_over = False
    
    def get_cell_from_pos(self, pos):
        x, y = pos
        row = y // CELL_SIZE
        col = x // CELL_SIZE
        if 0 <= row < 3 and 0 <= col < 3:
            return row, col
        return None
    
    def is_valid_move(self, row, col):
        return self.grid[row][col] == '' and not self.game_over
    
    def make_move(self, row, col):
        if self.is_valid_move(row, col):
            self.grid[row][col] = self.current_player
            if self.check_winner(row, col):
                self.winner = self.current_player
                self.game_over = True
            elif self.is_board_full():
                self.game_over = True
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False
    
    def check_winner(self, row, col):
        # Check row
        if all(self.grid[row][c] == self.current_player for c in range(3)):
            return True
        # Check column
        if all(self.grid[r][col] == self.current_player for r in range(3)):
            return True
        # Check diagonals
        if row == col and all(self.grid[i][i] == self.current_player for i in range(3)):
            return True
        if row + col == 2 and all(self.grid[i][2-i] == self.current_player for i in range(3)):
            return True
        return False
    
    def is_board_full(self):
        return all(self.grid[row][col] != '' for row in range(3) for col in range(3))

def draw_grid():
    # Draw vertical lines
    for x in range(CELL_SIZE, SCREEN_SIZE, CELL_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (x, 0), (x, SCREEN_SIZE), LINE_WIDTH)
    
    # Draw horizontal lines
    for y in range(CELL_SIZE, SCREEN_SIZE, CELL_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (0, y), (SCREEN_SIZE, y), LINE_WIDTH)

def draw_symbols(board):
    for row in range(3):
        for col in range(3):
            center_x = col * CELL_SIZE + CELL_SIZE // 2
            center_y = row * CELL_SIZE + CELL_SIZE // 2
            if board.grid[row][col] == 'X':
                # Draw X
                start_x = center_x - CELL_SIZE // 2 + SYMBOL_MARGIN
                end_x = center_x + CELL_SIZE // 2 - SYMBOL_MARGIN
                start_y = center_y - CELL_SIZE // 2 + SYMBOL_MARGIN
                end_y = center_y + CELL_SIZE // 2 - SYMBOL_MARGIN
                pygame.draw.line(screen, X_COLOR, (start_x, start_y), (end_x, end_y), SYMBOL_WIDTH)
                pygame.draw.line(screen, X_COLOR, (start_x, end_y), (end_x, start_y), SYMBOL_WIDTH)
            elif board.grid[row][col] == 'O':
                # Draw O
                radius = CELL_SIZE // 2 - SYMBOL_MARGIN
                pygame.draw.circle(screen, O_COLOR, (center_x, center_y), radius, SYMBOL_WIDTH)

def draw_status(board):
    # Initialize font
    font = pygame.font.Font(None, FONT_SIZE)
    
    if board.game_over:
        if board.winner:
            text = f"Player {board.winner} wins! Press R to restart"
        else:
            text = "It's a draw! Press R to restart"
    else:
        text = f"Player {board.current_player}'s turn"
    
    # Create text surface
    text_surface = font.render(text, True, LINE_COLOR)
    text_rect = text_surface.get_rect(center=(SCREEN_SIZE // 2, SCREEN_SIZE - 30))
    screen.blit(text_surface, text_rect)

def main():
    running = True
    board = Board()
    
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not board.game_over:
                # Handle mouse clicks
                mouse_pos = pygame.mouse.get_pos()
                cell = board.get_cell_from_pos(mouse_pos)
                if cell:
                    row, col = cell
                    board.make_move(row, col)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Reset game when 'R' is pressed
                    board.reset_game()
            
        # Fill the screen with background color
        screen.fill(BACKGROUND_COLOR)
        
        # Draw the grid
        draw_grid()
        
        # Draw X's and O's
        draw_symbols(board)
        
        # Draw game status
        draw_status(board)
        
        # Update the display
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
