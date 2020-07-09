from fractions import Fraction
from fractions import gcd

def inv(A):

    n = len(A)

    table = [[0]*2*n for _ in xrange(n)]  # Create an empty table

    # Copy initial values
    for i in range(n):
        for j in range(n):
            table[i][j] = A[i][j]
        table[i][i+n] = 1  # Diagonal matrix


    for i in range(n):  # For each row
        scalar = table[i][i]

        for j in range(2*n):
            table[i][j] /= scalar

        for j in range(n):
            if j != i:
                scalar = table[j][i]
                for k in range(2*n):
                    table[j][k] -= scalar * table[i][k]

    B = [table[i][n:] for i in range(n)]  # Paste the result
    return B


def get_transition_matrix(m):
    n = len(m)

    P = [[0]*n for _ in xrange(n)]  # Initialize matrix

    map_states_tra = {}  # Transitional states
    map_states_abs = {}  # Finals states

    for i in range(n):
        total_weights = sum(m[i])
        if total_weights == 0:
            map_states_abs[i] = len(map_states_abs)

            pos = n - len(map_states_abs)  # Diagonal matrix
            P[pos][pos] = 1  # TODO: Use fraction instead ?
        else:
            map_states_tra[i] = len(map_states_tra)

            for j in range(n):  # Normalize the weights
                m[i][j] = Fraction(m[i][j],total_weights)

    len_tran = len(map_states_tra)
    for k, v in map_states_abs.iteritems():  # Shift the ids (keep the same order of final state so we don't have to resort the idx at the end)
        map_states_abs[k] += len_tran

    map_states_tra.update(map_states_abs)
    map_states = map_states_tra

    inv_map_states = {v: k for k, v in map_states.iteritems()}
    for i in range(len_tran):
        for j in range(n):
            P[i][j] = m[inv_map_states[i]][inv_map_states[j]]

    Q = [x[0:len_tran] for x in P[0:len_tran]]
    R = [x[len_tran:] for x in P[0:len_tran]]

    return Q, R


def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def normalize_probs(probs):
    """ Compute the global least common multiple and return the probabilities
    in the asked format
    """
    lcm_glob = reduce(lcm, [fract.denominator for fract in probs])

    normalized_probs = [fract.numerator * lcm_glob // fract.denominator for fract in probs]
    normalized_probs.append(lcm_glob)

    return normalized_probs



def answer(m):

    if sum(m[0]) == 0:
        return [1, 1]

    Q, R = get_transition_matrix(m)

    for i in range(len(Q)):
        Q[i][i] -= 1
    F = inv(Q)  # F = -(I-Q)^-1 (WARNING: Opposite sign)

    probs = []
    for i in range(len(R[0])):
        cell = 0
        for j in range(len(F)):
            cell += -F[0][j]*R[j][i]  # (WARNING: We correct the negative sign here)
        probs.append(cell)

    probs_normalized = normalize_probs(probs)
    return probs_normalized