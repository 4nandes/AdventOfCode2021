from copy import deepcopy

def polymerEngine(buckets,bucketMap,blankBuckets,clockStopTime,letters):
    clock = 0
    while clock != clockStopTime:
        clock += 1
        bucketAdd = deepcopy(blankBuckets)
        bucketSub = deepcopy(blankBuckets)
        for bucket in buckets.keys():
            bucketAdd[bucket[:1]+bucketMap[bucket]] += buckets[bucket]
            bucketAdd[bucketMap[bucket]+bucket[1:]] += buckets[bucket]
            bucketSub[bucket] += buckets[bucket]
            # print(bucketMap[bucket], " ", buckets[bucket])
            if bucketMap[bucket] in letters:
                letters[bucketMap[bucket]] += buckets[bucket]
            else:
                letters[bucketMap[bucket]] = buckets[bucket]
        for adder in bucketAdd.keys():
            buckets[adder] += bucketAdd[adder]
        for subber in bucketSub.keys():
            buckets[subber] -= bucketSub[subber]
    scores = sorted((value) for (key,value) in letters.items())
    return (scores[len(scores)-1]-scores[0])

def polymerStarter(start, buckets,letters):
    for x in range(0,len(start)-1):
        buckets[start[x:x+2]] += 1
    for x in start:
        if x in letters:
            letters[x] += 1
        else:
            letters[x] = 1
    return

def bucketFoundationMaker(data):
    bucketMap = {}
    buckets = {}
    for bucket in data:
        bucket = bucket.split(" -> ")
        bucketMap[bucket[0]] = bucket[1]
        buckets[bucket[0]] = 0
    return bucketMap, buckets
    pass

if __name__ == '__main__':
    # Build the information
    data = [x[:-1] for x in open("day14input","r")]
    bucketMap, buckets = bucketFoundationMaker(data[2:])
    blankBuckets = deepcopy(buckets)
    letters = {}
    polymerStarter(data[:1][0], buckets, letters)
    
    # Part One
    print(polymerEngine(buckets,bucketMap,blankBuckets,10,letters))
    
    # Reset for Part Two
    buckets = deepcopy(blankBuckets)
    letters = {}
    polymerStarter(data[:1][0], buckets, letters)
    
    # Part Two
    print(polymerEngine(buckets,bucketMap,blankBuckets,40,letters))