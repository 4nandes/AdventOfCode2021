def getMiddle(scores):
    scores.sort()
    return scores[int((len(scores)/2)+ 0.5)- 1]

def getScore(remainingBrackets):
    score = 0
    bracketScores ={"(":1, "[":2, "{":3, "<":4}
    while len(remainingBrackets) != 0:
        score = (score * 5) + bracketScores[remainingBrackets.pop()]
    return score

def getBreak(brackets):
    queue = []
    score = {")":3, "]":57, "}":1197, ">":25137}
    for character in brackets:
        match character:
            case ")":
                if queue.pop() != "(":
                    return score[character]
            case "]":
                if queue.pop() != "[":
                    return score[character]
            case "}":
                if queue.pop() != "{":
                    return score[character]
            case ">":
                if queue.pop() != "<":
                    return score[character]
            case _:
                queue.append(character)
    return (getScore(queue) * -1)

if __name__ == '__main__':
    data = [x[:-1] for x in open("day10input","r")]

    # Part One
    print(sum([getBreak(line) if getBreak(line) > 0 else 0 for line in data]))

    # Part Two
    print(getMiddle([(getBreak(line) * -1) for line in data if getBreak(line) < 0]))