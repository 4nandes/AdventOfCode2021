import statistics

if __name__ == '__main__':
    data = [int(y) for y in "".join([x[:-1] for x in open("inputDay7.txt","r")]).split(",")]
    data.sort()
    
    # Part 1
    middlePoint = statistics.median(data)
    print(sum([int(abs(x - middlePoint)) for x in data]))
    
    # Part 2    
    fuelCost = [int(sum([((abs(x - location)*(1 + abs(x - location)))/2) for x in data])) for location in range(0,data[len(data)-1])]
    fuelCost.sort()
    print(fuelCost[0])