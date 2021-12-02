# Same as Day1Challenge1 but a 3 wide sliding window
def slidingWindowScan(data):
    count = 0
    for x in range(0, (len(data)-3)):
        if (data[x] < data[x+3]):
            count += 1
    return count

if __name__ == '__main__':
    data = [int(x) for x in open('../Day1Challenge1','r')]
    print(slidingWindowScan(data))