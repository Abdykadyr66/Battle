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
def process_shot(board, shot, ships):
    row = int(shot[1]) - 1
    col = ord(shot[0].upper()) - ord('A')
    
    if row < 0 or row >= 7 or col < 0 or col >= 7:
        return "out_of_bounds", board
    
    if board[row][col] == "X" or board[row][col] == "O":
        return "already_shot", board
    
    if board[row][col] == "S":  
        board[row][col] = "X"
        for ship in ships:
            if all(board[r][c] == "X" for r, c in ship):
                for r, c in ship:
                    board[r][c] = "D"
                return "sunk", board
        return "hit", board
    
    else:
        board[row][col] = "O"
        return "miss", board
def all_ships_sunk(board):
    return all(cell != "S" for row in board for cell in row)


def play_game():
    player_name = input("Enter your name: ")
    
    board = create_empty_board()
    ships = []
    ships.append(place_ship(board, 3))  
    ships.append(place_ship(board, 2))  
    ships.append(place_ship(board, 2))
    ships.append(place_ship(board, 1))  
    ships.append(place_ship(board, 1))
    ships.append(place_ship(board, 1))
    ships.append(place_ship(board, 1))
    
    shots_taken = 0
    clear_screen()
 while not all_ships_sunk(board):
        display_board(board)  
        shot = input(f"Player {player_name}, enter your shot (e.g., A1): ").upper()
        
        if len(shot) < 2 or not ('A' <= shot[0] <= 'G') or not ('1' <= shot[1] <= '7'):
            print("Invalid input! Please enter a valid shot (e.g., A1).")
            continue
        
        shots_taken += 1
        result, updated_board = process_shot(board, shot, ships)
        board = updated_board
        clear_screen()
        
        if result == "out_of_bounds":
            print("You shot out of bounds! Try again.")
        elif result == "already_shot":
            print("You already shot here! Try again.")
        elif result == "hit":
            print("You hit a ship!")
        elif result == "miss":
            print("You missed!")
        elif result == "sunk":
            print("You sunk a ship!")
        
        display_board(board)
    
    print(f"Congratulations, {player_name}! You've sunk all the ships in {shots_taken} shots.")
    
    return shots_taken
def main():
    player_scores = []
    while True:
        shots_taken = play_game()
        player_scores.append(shots_taken)
        
        replay = input("Do you want to play again? (yes/no): ").lower()
        if replay == "no":
            break
    print("\nLeaderboard:")
    for i, score in enumerate(sorted(player_scores)):
        print(f"Player {i + 1}: {score} shots")

if __name__ == "__main__":
    main()



  
