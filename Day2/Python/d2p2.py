def  coordinateFinder(data):
    horizontal = 0
    aim = 0
    depth = 0
    for x in data:
        match x.split(" ")[0]:
            case "forward":
                horizontal += int(x.split(" ")[1])
                depth += (aim * int(x.split(" ")[1]))
            case "down":
                aim += int(x.split(" ")[1])
            case "up":
                aim += (int(x.split(" ")[1])*-1)
    return(horizontal*depth)

if __name__ == '__main__':
    data = [x[:-1] for x in open("../day2input","r")] 
    print(coordinateFinder(data))