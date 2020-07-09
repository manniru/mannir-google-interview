def answer(pegs):
    maximum = pegs[1] - pegs[0] - 1
    for x in xrange(1, maximum):
        gear_sizes = [x]
        for peg in xrange(1, len(pegs)):
            gear_sizes.append(pegs[peg] - (pegs[peg-1] + gear_sizes[-1]))

        if any(d <= 0 for d in gear_sizes):
            continue

        if x == 2 * gear_sizes[-1]:
            return [x, 1]

        if x+1 == 2 * gear_sizes[-1]:
            return [(x * 3) + 1, 3]
        if x+2 == 2 * gear_sizes[-1]:
            return [(x * 3) + 2, 3]

    return [-1, -1]
