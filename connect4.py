from connect4board import generate_board
from generate_everything import generate_everything
ROWS = 6
COLUMNS = 7

def create_board():
    return [[' ' for _ in range(COLUMNS)] for _ in range(ROWS)]

def drop_piece(board, column, piece):
    for row in reversed(board):
        if row[column] == ' ':
            row[column] = piece
            return True
    return False

def check_win(board, piece):
    # Horizontal
    for row in range(ROWS):
        for col in range(COLUMNS - 3):
            if all(board[row][col+i] == piece for i in range(4)):
                return True

    # Vertical
    for col in range(COLUMNS):
        for row in range(ROWS - 3):
            if all(board[row+i][col] == piece for i in range(4)):
                return True

    # Diagonal /
    for row in range(3, ROWS):
        for col in range(COLUMNS - 3):
            if all(board[row-i][col+i] == piece for i in range(4)):
                return True

    # Diagonal \
    for row in range(ROWS - 3):
        for col in range(COLUMNS - 3):
            if all(board[row+i][col+i] == piece for i in range(4)):
                return True

    return False

def play_game():
    board=create_board()
    game_over = False
    turn = 0

# cia pridedu kad sugeneruotu ir empty lenta
    generate_board(board)

    while not game_over:

        generate_everything()

        piece = 'X' if turn % 2 == 0 else 'O'

        try:
            column=input(f"Player {piece}, choose a column (1-{COLUMNS}): ")
            column = int(column)
            if 1<=column<=COLUMNS:
                column -= 1
                if drop_piece(board, column, piece):
                    generate_board(board)
                    generate_everything()
                    if check_win(board, piece):
                        print(f"Player {piece} wins!")
                        game_over = True
                    else:
                        turn += 1
                        if turn == ROWS * COLUMNS:
                            print("It's a draw!")
                            game_over = True
                else:
                    print("Column is full! Try again.")
            else:
                print(f"Invalid column. Choose a number between 1 and {COLUMNS}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

        
        

if __name__ == "__main__":
    play_game()