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

  
