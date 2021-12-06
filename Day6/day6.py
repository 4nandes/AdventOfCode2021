def lanternCounter(data, days):
    ninePool = [0,0,0,0,0,0,0,0,0]
    for x in data:
        ninePool[x] += 1
    for x in range(0,days):
        newLanterns = ninePool[0]
        ninePool = [ninePool[x+1] if x < 8 else 0 for x in range(0, len(ninePool))]
        ninePool[6] += newLanterns
        ninePool[8] += newLanterns
    return ninePool

if __name__ == '__main__':
    data = [int(y) for y in "".join([x[:-1] for x in open("lanterns.txt","r")]).split(",")]

    # Part 1
    print(sum([int(x) for x in lanternCounter(data, 80)]))

    # Part 2
    print(sum([int(x) for x in lanternCounter(data, 256)]))