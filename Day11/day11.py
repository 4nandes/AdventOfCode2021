def scoreOrSync(grid,score, clock,part):
    sync = 0
    for x in range(1,len(grid)-1):
        for y in range(1,len(grid)-1):
            if grid[x][y] > 9:
                grid[x][y] = 0
                score += 1
                sync += 1
    clock += 1
    if clock == 100 and part == 0:
        return score
    if sync == 100:
        return clock
    return cycle(grid,score,clock,part)

def flash(grid, flashed,x,y):
    if (0 < x < len(grid)-1) and (0 < y < len(grid)-1):
        flashed[x][y] = 1
        grid[x-1][y]  += 1
        grid[x+1][y]  += 1
        grid[x][y-1]  += 1
        grid[x][y+1]  += 1
        grid[x+1][y+1] += 1
        grid[x+1][y-1] += 1
        grid[x-1][y+1] += 1
        grid[x-1][y-1] += 1
        if grid[x-1][y] > 9 and flashed[x-1][y] == 0:
            flash(grid,flashed,x-1,y)
        if grid[x+1][y] > 9 and flashed[x+1][y] == 0:
            flash(grid,flashed,x+1,y)
        if grid[x][y-1] > 9 and flashed[x][y-1] == 0:
            flash(grid,flashed,x,y-1)
        if grid[x][y+1] > 9 and flashed[x][y+1] == 0:
            flash(grid,flashed,x,y+1)
        if grid[x+1][y+1] > 9 and flashed[x+1][y+1] == 0:
            flash(grid,flashed,x+1,y+1)
        if grid[x+1][y-1] > 9 and flashed[x+1][y-1] == 0:
            flash(grid,flashed,x+1,y-1)
        if grid[x-1][y+1] > 9 and flashed[x-1][y+1] == 0:
            flash(grid,flashed,x-1,y+1)
        if grid[x-1][y-1] > 9 and flashed[x-1][y-1] == 0:
            flash(grid,flashed,x-1,y-1)
    return 

def cycle(grid,score,clock,part):
    for x in range(1,len(grid)-1):
        for y in range(1,len(grid)-1):
            grid[x][y] += 1
    flashed =[[0 for y in range(0, len(grid))] for x in range(0,len(grid))]
    for x in range(1,len(grid)-1):
        for y in range(1,len(grid)-1):
            if grid[x][y] > 9 and flashed[x][y] == 0:
                flash(grid,flashed,x,y)
    return scoreOrSync(grid,score,clock,part)

if __name__ == '__main__':
    data = [([9] + [int(y) for y in x[:-1]] + [9]) for x in open("day11input","r")]
    ninePad = [9 for x in range(0,len(data[0]))]
    data = [ninePad] + data + [ninePad]
    # Part One
    print(cycle(data,0,0,0))

    # Part Two
    print(cycle(data,0,0,1) + 100)
    