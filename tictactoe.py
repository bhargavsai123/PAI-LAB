board = [" "] * 9

def win(p):
    w = [(0,1,2),(3,4,5),(6,7,8),
         (0,3,6),(1,4,7),(2,5,8),
         (0,4,8),(2,4,6)]
    return any(board[a]==board[b]==board[c]==p for a,b,c in w)

def alphabeta(isMax, alpha, beta):
    if win("O"): return 1
    if win("X"): return -1
    if " " not in board: return 0

    if isMax:  # AI (O)
        best = -100
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                best = max(best, alphabeta(False, alpha, beta))
                board[i] = " "
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
        return best
    else:      # Human (X)
        best = 100
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                best = min(best, alphabeta(True, alpha, beta))
                board[i] = " "
                beta = min(beta, best)
                if beta <= alpha:
                    break
        return best

def best_move():
    best = -100
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = alphabeta(False, -100, 100)
            board[i] = " "
            if score > best:
                best = score
                move = i
    return move

def print_board():
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])

while True:
    print_board()

    # Safe user input
    while True:
        try:
            pos = int(input("Enter your move (0-8): "))
            if pos < 0 or pos > 8:
                print("Position must be between 0 and 8.")
            elif board[pos] != " ":
                print("Cell already occupied. Try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Enter a number.")

    board[pos] = "X"

    if win("X"):
        print_board()
        print("You win!")
        break

    ai = best_move()
    board[ai] = "O"
    print("AI move:", ai)

    if win("O"):
        print_board()
        print("AI wins!")
        break

    if " " not in board:
        print_board()
        print("Draw!")
        break
