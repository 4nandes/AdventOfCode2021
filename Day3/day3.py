def deltaGamma(data):
    binaryBuilder = [0,0,0,0,0,0,0,0,0,0,0,0]
    for x in data:
        for y in range(0,12):
            binaryBuilder[y] += int(x[y])
    gamma = "".join(["1" if (int(x) > (len(data)/2)) else "0" for x in binaryBuilder]) 
    return (int(gamma,2)*int("".join(["1" if x == "0" else "0" for x in gamma]),2))

def oxygenCarbon(data,oxOrCarb):
    column = 0
    while len(data) != 1:
        count = sum([int(x[column]) for x in data])
        data = [x for x in data if int(x[column]) == ((2 if count < (len(data)/2) else 3)+oxOrCarb)%2]
        column += 1
    return int(data[0],2)

if __name__ == '__main__':
    data = [x[:-1] for x in open('inputDay3','r')]

    # first challenge
    print(deltaGamma(data))

    # second challenge
    print(oxygenCarbon(data,0)*oxygenCarbon(data,1))