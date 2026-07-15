class Board:
    def __init__(self):
        self.board : list[list[str]] = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.currentPlayer: str = 'X'

    def changePlayer(self) -> None:
        if self.currentPlayer == 'X':
            self.currentPlayer = 'O'
        else:
            self.currentPlayer = 'X'
    
    def checkWin(self) -> bool | str:
        if (self.board[0][0] != ' '
            and self.board[0][0] == self.board[1][1]
            and self.board[1][1] == self.board[2][2]):
            return self.board[0][0]
        
        if (self.board[0][2] != ' '
            and self.board[0][2] == self.board[1][1]
            and self.board[1][1] == self.board[2][0]):
            return self.board[0][2]
        
        for i in range(0 ,3):
            if (self.board[i][0] != ' '
            and self.board[i][0] == self.board[i][1]
            and self.board[i][1] == self.board[i][2]):
                return self.board[i][0]
            
            if (self.board[0][i] != ' '
            and self.board[0][i] == self.board[1][i]
            and self.board[1][i] == self.board[2][i]):
                return self.board[0][i]
        return False

    def addToBoard(self, position: int) -> tuple[bool, str]:
        row = None
        col = None
        match position:
            case position if 7 <= position <= 9:
                row = 0
                col = position - 7
            
            case position if 4 <= position <= 6:
                row = 0
                col = position - 4
            
            case position if 1 <= position <= 3:
                row = 0
                col = position - 1
            
            case _:
                return (False, 'Error: Position is out of range!')

        if self.board[row][col] != ' ':
            return (False, 'Error: the position is not Empty')

        self.board[row][col] = self.currentPlayer
        self.changePlayer()

        return (True, '')


