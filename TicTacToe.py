# Tic tac toe with a simple Ai (credits to Tech with Tim for inspiration)

board = [' ' for x in range(10)]
playerPiece = 'X'
computerPiece = 'O'


def playMove(piece, square):
    board[square] = piece


def squareIsEmpty(square):
    return board[square] == ' '


def printBoard(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])


def wonGame(board, piece):
    # checks all 8 possible winning results
    return ((board[7] == piece and board[8] == piece and board[9] == piece) or
            (board[4] == piece and board[5] == piece and board[6] == piece) or
            (board[1] == piece and board[2] == piece and board[3] == piece) or
            (board[7] == piece and board[4] == piece and board[1] == piece) or
            (board[8] == piece and board[5] == piece and board[2] == piece) or
            (board[9] == piece and board[6] == piece and board[3] == piece) or
            (board[7] == piece and board[5] == piece and board[3] == piece) or
            (board[9] == piece and board[5] == piece and board[1] == piece))


def playerMove():
    while True:
        square = input('Please select a square(1-9) to place your piece: ')
        try:
            square = int(square)
            if 0 < square < 10:
                if squareIsEmpty(square):
                    playMove(playerPiece, square)
                    break
                else:
                    print('This square is occupied!')
            else:
                print('Please type a number within the range(1-9)!')

        except ValueError:
            print('Please type a number!')


def selectCompMove():
    possibleMoves = [x for x, piece in enumerate(board) if piece == ' ' and x != 0]
    move = 0

    for piece in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = piece
            if wonGame(boardCopy, piece):
                move = i
                return move

    # play in center first if possible
    if 5 in possibleMoves:
        move = 5
        return move

    # play in the corner next
    cornerMoves = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornerMoves.append(i)

    if len(cornerMoves) > 0:
        move = selectRandom(cornerMoves)
        return move

    # play on the edges last
    edgeMoves = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgeMoves.append(i)

    if len(edgeMoves) > 0:
        move = selectRandom(edgeMoves)

    return move


def playComputerMove():
    move = selectCompMove()
    if move != 0:
        playMove(computerPiece, move)
        print('Computer played at square', move, ':')


def selectRandom(list):
    import random
    length = len(list)
    r = random.randrange(0, length)
    return list[r]


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def main():
    print('Thank you for playing Tic Tac Toe!')
    printBoard(board)
    response = input('Would you like to go first? (Y/N)')
    if response.lower() == 'n' or response.lower == 'no':
        global playerPiece, computerPiece
        playerPiece = 'O'
        computerPiece = 'X'
        playComputerMove()
        printBoard(board)

    while not (isBoardFull(board)):
        if not (wonGame(board, computerPiece)):
            playerMove()
            printBoard(board)
            if isBoardFull(board):
                break
        else:
            print('You lost!')
            break

        if not (wonGame(board, playerPiece)):
            playComputerMove()
            printBoard(board)
        else:
            print('You won, great job!')
            break

    if isBoardFull(board):
        print('Draw!')


while True:
    answer = input('Another game? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(10)]
        print('----------------------------------')
        main()
    else:
        break
