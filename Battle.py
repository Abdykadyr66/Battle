import random
import os
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')
  def display_board(board, reveal=False):
    print("  A B C D E F G")
    for row in range(7):
        display_row = []
        for col in range(7):
            cell = board[row][col]
            if not reveal:
                if cell == "S":  
                    display_row.append(" ")
                else:
                    display_row.append(cell)
            else:
                display_row.append(cell)
        print(f"{row+1} {' '.join(display_row)}")
def create_empty_board():
    return [[" " for _ in range(7)] for _ in range(7)]
def is_valid_position(board, ship):
    for (r, c) in ship:      
        if r < 0 or r >= 7 or c < 0 or c >= 7:
            return False
        if board[r][c] == "S" or board[r][c] == "X":
            return False
 for (r, c) in ship:
        for i in range(-1, 2):
            for j in range(-1, 2):
                nr, nc = r + i, c + j
                if 0 <= nr < 7 and 0 <= nc < 7 and board[nr][nc] == "S":
                    return False

    return True
def place_ship(board, size):
    while True:
        orientation = random.choice(["H", "V"])  
        row = random.randint(0, 6)
        col = random.randint(0, 6)

        if orientation == "H" and col + size <= 7:
            ship = [(row, col + i) for i in range(size)]
            if is_valid_position(board, ship):
                for (r, c) in ship:
                    board[r][c] = "S"
                return ship
        elif orientation == "V" and row + size <= 7:
            ship = [(row + i, col) for i in range(size)]
            if is_valid_position(board, ship):
                for (r, c) in ship:
                    board[r][c] = "S"  
                return ship

  
