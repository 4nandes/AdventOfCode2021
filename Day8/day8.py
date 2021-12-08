def decodeSum(code,pin):
    one = ""
    seven = ""
    four = ""
    eight = ""
    for x in code:
        match len(x):
            case 2:
                one = x
            case 3:
                seven = x
            case 4:
                four = x
            case 7:
                eight = x
    newPin = ""
    for x in pin:
        match len(x):
            case 2:
                newPin += "1"
            case 3:
                newPin += "7"
            case 4:
                newPin += "4"
            case 5:
                if sum([1 if letter in seven else 0 for letter in x]) == 3:
                    newPin += "3"
                else:
                    if sum([1 if letter in four else 0 for letter in x]) == 2:
                        newPin += "2"
                    else:
                        newPin += "5"
            case 6:
                if sum([1 if letter in four else 0 for letter in x]) == 4:
                    newPin += "9"
                elif sum([1 if letter in seven else 0 for letter in x]) == 3:
                    newPin += "0"
                else:
                    newPin += "6"
            case 7:
                newPin += "8"
    return int(newPin)

if __name__ == '__main__':

    data = [[x[:-1].split("|")[0].split(" ")[:-1],x[:-1].split("|")[1].split(" ")[1:]] for x in open('inputDay8','r')]
    
    # Part One
    print(sum([sum([1 if len(y) in [2,3,4,7] else 0 for y in x[1]]) for x in data]))
    
    #Part Two
    print(sum([decodeSum(what[0],what[1]) for what in [[y for y in x] for x in data]]))
    
    
    