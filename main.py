from board import Board

game = Board()
gameTurns = 0
isWin = False
game.printNumberedBoard()

while gameTurns < 9 and not isWin:
    positionInput = int(input(f"Enter a position for player {str(game.currentPlayer)} >>>> "))

    isAddedToBoard = game.addToBoard(positionInput)

    if isAddedToBoard[0]:
        gameTurns = gameTurns + 1
    else:
        print(isAddedToBoard[1])

    game.printTheBoard()

    if gameTurns >= 5:
        winner = game.checkWin()
        if isinstance(winner, bool):
            pass
        else:
            print(f'{winner} has WON!')
            isWin = True
            break

if not isWin:
    print('It is draw!')