def floodValue(startingPoint, grid, visited):
    queue = []
    queue.append(startingPoint)
    total = 0
    while len(queue) != 0:
        current = queue.pop()
        if grid[current[0]] [current[1]] == 9:
            continue
        if visited[current[0]][current[1]] == 1:
            continue
        visited[current[0]][current[1]] = 1
        total += 1
        queue.insert(0,[current[0] + 1,current[1]])
        queue.insert(0,[current[0] - 1,current[1]]) 
        queue.insert(0,[current[0],current[1] + 1]) 
        queue.insert(0,[current[0],current[1] - 1]) 
    return total

def bfsEngine(lowPoints, grid):
    visited = [[0 for x in range(0,len(grid[0]))] for y in range(0,len(grid))]
    scores = []
    for x in lowPoints:
        scores.append(floodValue(x, grid, visited))
    scores.sort()
    return scores[-3:]
    

def findLowpoints(grid):
    lowPoints = []
    for x in range(1,len(grid)-1):
        for y in range(1, len(grid[0])-1):
            # forgive me father, for I have sinned
            if ((grid[x][y] < grid[x-1][y]) 
            and (grid[x][y] < grid[x+1][y]) 
            and (grid[x][y] < grid[x][y-1]) 
            and (grid[x][y] < grid[x][y+1]) 
            and (grid[x][y] < grid[x+1][y+1]) 
            and (grid[x][y] < grid[x+1][y-1]) 
            and (grid[x][y] < grid[x-1][y+1]) 
            and (grid[x][y] < grid[x-1][y-1])):
                lowPoints.append([x,y])
    return lowPoints

if __name__ == '__main__':
    grid =[([9] + [int(y) for y in x[:-1]] + [9]) for x in open("day9input", "r")]
    ninePad = [9 for x in range(0,len(grid[0]))]
    grid = [ninePad] + grid + [ninePad]

    # Part 1
    lowPoints = findLowpoints(grid)
    print(sum([grid[x[0]][x[1]] + 1 for x in lowPoints]))

    # Part 2
    flag = 0
    for x in bfsEngine(lowPoints,grid):
        if flag == 0:
            flag += x
        else:
            flag = flag * x
    print(flag)

    