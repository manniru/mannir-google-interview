import itertools

def get_best(current, candidate):

    if len(candidate) > len(current):
        return sorted(list(candidate))
    elif len(candidate) == len(candidate):
        candidate = sorted(list(candidate))
        for i in range(len(current)):
            if current[i] < candidate[i]:
                return current
            elif current[i] > candidate[i]:
                return candidate
    return current


def answer(times, time_limit):
    nb_pos = len(times)
    nb_bunnies = nb_pos-2
    assert nb_bunnies > 0

    moves = [[None]*nb_pos for _ in xrange(nb_pos)]

    paths = itertools.chain(*map(
        lambda path_length: itertools.permutations(range(nb_pos), path_length),
        range(2, nb_pos+1)
    ))
    for path in paths:
        origin = path[0]
        destination = path[-1]

        cost = 0
        prev_pos = origin
        for pos in path:
            cost += times[prev_pos][pos]
            prev_pos = pos

        if moves[origin][destination] == None or cost < moves[origin][destination]:
            moves[origin][destination] = cost

        cost += times[destination][origin]
        if cost < 0:
            return range(nb_bunnies)

    bunnies_saved = []
    paths = itertools.chain(*map(  # All bunnies combinations in all possibles orders
        lambda path_length: itertools.permutations(range(nb_bunnies), path_length),
        range(0, nb_bunnies+1)
    ))
    for path in paths:
        origin = 0
        destination = nb_pos-1

        time = time_limit
        prev_pos = origin
        for pos in path:
            time -= moves[prev_pos][pos+1]
            prev_pos = pos+1  # We shift the ids (bunnies 0 start at 1)
        time -= moves[prev_pos][destination]

        if time >= 0:
            bunnies_saved = get_best(bunnies_saved, path)

    return bunnies_saved