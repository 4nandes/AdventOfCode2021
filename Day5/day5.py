def tallyUp(board):
    score = 0
    for x in board:
        for y in x:
            if int(y) > 1:
                score += 1
    return score

def diagonalMarks(board,y, start, end, upDown):
    for x in range(start, end+1):
        board[y][x] += 1
        if upDown == 0:
            y += 1
        else:
            y = y -1
    return

def markBoard(board, xOry, start, end, horVert):
    if start > end:
        start, end = end, start
    for x in range(start, end+1):
        if horVert == 0:
            board[x][xOry] += 1
        else:
            board[xOry][x] += 1
    return

def iterateCoords(coords, board):
    for coord in coords:
        breakDown = coord.split(" ")
        start = [int(x) for x in breakDown[0].split(",")]
        end = [int(x) for x in breakDown[2].split(",")]
        if start[0] > end[0]:
            start, end = end, start
        if (start[0] == end[0]):
            markBoard(board, start[0], start[1], end[1], 0)
        elif (start[1] == end[1]):
            markBoard(board, start[1], start[0], end[0], 1)
        else:
            if start[1] < end[1]:
                diagonalMarks(board, start[1], start[0], end[0], 0)
            else:
                diagonalMarks(board, start[1], start[0], end[0], 1)
    return board


if __name__ == '__main__':
    data = [x[:-1] for x in open("inputDay5.txt","r")] 
    board = [[0 for x in range(0,1500)] for x in range(0,1000)]
    board = iterateCoords(data,board)
    print(tallyUp(board))
