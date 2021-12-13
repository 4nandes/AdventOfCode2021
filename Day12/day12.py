from copy import deepcopy

def twoHopsThisTime(start,map,journey,victories,littleGuy):
    journey = deepcopy(journey)
    journey.append(start)
    if start == "end":
        victories.append(journey)
        return
    for x in map[start]:
        if x == littleGuy:
            if ((journey.count(x) <= 1) or x.isupper()) and x != "start":
                twoHopsThisTime(x,map,journey,victories,littleGuy)
        else:
            if (x not in journey or x.isupper()) and x != "start":
                twoHopsThisTime(x,map,journey,victories,littleGuy)
    pass

def explore(start,map,journey,victories):
    journey = deepcopy(journey)
    journey.append(start)
    if start == "end":
        victories.append(journey)
        pass
    for x in map[start]:
        if x not in journey or x.isupper():
            explore(x,map,journey,victories)
    pass

def mapMaker(edges):
    map = {}
    for edge in edges:
        edge = edge.split("-")
        if edge[0] in map:
            map[edge[0]].append(edge[1])
        else:
            map[edge[0]] = [(edge[1])]
        if edge[1] in map:
            map[edge[1]].append(edge[0])
        else:
            map[edge[1]] = [(edge[0])]
    return map

if __name__ == '__main__':
    edges = [x[:-1] for x in open("day12input.txt", "r")]
    
    map = mapMaker(edges)
    journey = []
    victories = []
    explore("start",map, journey,victories)
    partOne = len(victories)
    print(partOne)

    victories = []
    journey = []
    copyKillCount = 0
    for littleGuy in map:
        if littleGuy.islower() and littleGuy != "start" and littleGuy != "end":
            copyKillCount += 1
            twoHopsThisTime("start",map, journey,victories,littleGuy)
    print(len(victories)-((copyKillCount-1)*partOne))