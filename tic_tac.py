import random

def print_board(board):
    print()
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 13)
    print()

def check_winner(board, player):
    for row in board:
        if row.count(player) == 3:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    
    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 10 - depth
    if check_winner(board, 'X'):
        return depth - 10
    if is_board_full(board):
        return 0
    
    if is_maximizing:
        max_eval = float('-inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'O'
            eval_score = minimax(board, depth + 1, False)
            board[i][j] = ' '
            max_eval = max(max_eval, eval_score)
        return max_eval
    else:
        min_eval = float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'X'
            eval_score = minimax(board, depth + 1, True)
            board[i][j] = ' '
            min_eval = min(min_eval, eval_score)
        return min_eval

def best_move(board):
    best_val = float('-inf')
    best_move_pos = (-1, -1)
    
    for i, j in get_empty_cells(board):
        board[i][j] = 'O'
        move_val = minimax(board, 0, False)
        board[i][j] = ' '
        
        if move_val > best_val:
            best_move_pos = (i, j)
            best_val = move_val
    
    return best_move_pos

def get_player_move(board):
    while True:
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid input! Enter 0, 1, or 2 only.")
                continue
            
            if board[row][col] != ' ':
                print("Cell already occupied! Try again.")
                continue
            
            return row, col
        except ValueError:
            print("Invalid input! Enter numbers only.")
        except KeyboardInterrupt:
            print("\nGame ended by player.")
            exit()

def main():
    print("=" * 50)
    print("     TIC-TAC-TOE WITH AI ")
    print("=" * 50)
    
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player_turn = random.choice([True, False])
    
    print(f"\nStarting player: {'YOU (X)' if player_turn else 'AI (O)'}")
    
    while True:
        print_board(board)
        
        if player_turn:
            print("Your turn (X)")
            row, col = get_player_move(board)
            board[row][col] = 'X'
            
            if check_winner(board, 'X'):
                print_board(board)
                print("=" * 50)
                print("     🎉 CONGRATULATIONS! YOU WIN! 🎉")
                print("=" * 50)
                break
        else:
            print("AI's turn (O)")
            print("AI is thinking...")
            row, col = best_move(board)
            board[row][col] = 'O'
            print(f"AI placed O at position ({row}, {col})")
            
            if check_winner(board, 'O'):
                print_board(board)
                print("=" * 50)
                print("     AI WINS! Better luck next time!")
                print("=" * 50)
                break
        
        if is_board_full(board):
            print_board(board)
            print("=" * 50)
            print("     IT'S A TIE! Well played!")
            print("=" * 50)
            break
        
        player_turn = not player_turn
    
    play_again = input("\nWould you like to play again? (y/n): ").lower()
    if play_again == 'y':
        main()
    else:
        print("Thanks for playing! Goodbye!")

if __name__ == "__main__":
    main()
