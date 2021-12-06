# Approximate runtime complexity:
# O(embarassingly high)
# I couldnt come up with a better way to do this

def buildBoards(data):
    board = list()
    gameBoards = list()
    for x in data:
        if x == "":
            gameBoards.append(board)
            board = list()
        else:
            board.append([[0,int(y)] for y in x.split(" ") if y.isnumeric()])
    return gameBoards

def getScore(board):
    score = 0
    for x in board:
        for y in x:
            if y[0] == 0:
                score += y[1]
    return score

def isWinner(board):
    for y in range(0,5):
        if (sum([x[0] for x in board[y]]) == 5) or (sum([board[x][y][0] for x in range(0,5)]) == 5):
            return getScore(board)
    return 0


def blotter(board, ball):
    for x in range(0, 5):
        for y in range(0,5):
            if board[x][y][1] == ball:
                board[x][y][0] = 1
    return board

def bingoWinner(pulls,boards):
    for ball in pulls:
        for x in range(0,len(boards)):
            boards[x] = blotter(boards[x], ball)
            if isWinner(boards[x]) > 0:
                return isWinner(boards[x])*ball
    return boards

def bingoLoser(pulls,boards):
    remaining = [int(x) for x in range(0,len(boards))]
    for ball in pulls:
        for x in remaining:
            boards[x] = blotter(boards[x], ball)
            if isWinner(boards[x]) > 0:
                remaining.remove(x)
            if len(remaining) == 1:
                return isWinner(boards[x])*ball
            


if __name__ == '__main__':
    data = [x[:-1] for x in open("inputDay4.txt","r")] 
    bingoPulls = [int(x) for x in data[0].split(",")]
    gameBoards = buildBoards(data[2:])
    
    # Part 1
    print(bingoWinner(bingoPulls, gameBoards))
    # Part 2
    print(bingoLoser(bingoPulls, gameBoards))
    