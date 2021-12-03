# Youre in an xmas submarine, find out how many times the sonar reading increases in height.
def sonarscan(data):
    total = 0
    for x in range(0, len(data)):
        if (data[x-1] <= data[x]):
            total += 1
    return total

def slidingWindowScan(data):
    count = 0
    for x in range(0, (len(data)-3)):
        if (data[x] < data[x+3]):
            count += 1
    return count

if __name__ == '__main__':
    data = [int(x) for x in open('Day1Challenge1','r')]
    
    # Challenge 1 function
    print(sonarscan(data))

    # Challenge 2 function
    print(slidingWindowScan(data))