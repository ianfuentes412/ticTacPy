global board
board = [[" ", " ", " "],[" ", " ", " ",],[" ", " ", " "]]
player1 = "X"

def printBoard(board):
    for line in board:
        print(line)

def isWin():
    global player1
    if player1 == "X":
      p = "0"
    else:
      p = "X"


    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[x][y] != p:
                win = False
                break
        if win:
            return True
        
    for y in range(len(board)):
      win = True
      for x in range(len(board)):
        if board[x][y] != p:
          win = False
          break
      if win:
        return True

    win = True
    for y in range(3):
      if board[y][y] != p:
        win = False
        break
    if win:
      return True   
        
    win = True
    for x in range(len(board)):
      if board[x][len(board) - 1 - x] != p:
        win = False
        break

    return False

def tictac():
    printBoard(board)
    makeMove()
    isWin()

def makeMove():
    global player1
    x = int(input("Player" + player1 + ", X Coordinate? "))
    y = int(input("Y Coordinate? "))

    while board[x][y] != " ":
        print("You must choose an empty spot!")
        x = int(input("Player" + player1 + ", X Coordinate? "))
        y = int(input("Y Coordinate? "))

    if player1 == "X":
        board[x][y] = "X"
        player1 = "0"
    else:
        board[x][y] = "0"
        player1="X"

def main():
    gamewon = False
    while gamewon == False:
        tictac()
        gamewon = isWin()
    print("GAME!")


main()