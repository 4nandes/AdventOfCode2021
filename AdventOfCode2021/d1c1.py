def sonarscan(data):
    total = 0
    for x in range(0, len(data)):
        if (data[x-1] <= data[x]):
            total += 1
    return total

if __name__ == '__main__':
    data = [int(x) for x in open('./Day1Challenge1','r')]
    print(sonarscan(data))