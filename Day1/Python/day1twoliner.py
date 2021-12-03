data = [int(x) for x in open('../Day1Challenge1','r')]
print(sum([1 if (data[y-1] <= data[y]) else 0 for y in range(0,len(data))]))