def answer(M, F):
    M, F = int(M), int(F)
    gen = 0
    possible = False
    while M > 0 and F > 0:
        if M == 1 and F == 1:
            possible = True
            break
        elif M == F:
            break
        if M < F:
            M, F = F, M

        i = 1
        while M - F * i > 0:
            i *= 2
        i /= 2

        M = M - F * i
        gen += i

    if not possible:
        return 'impossible'
    else:
        return str(gen)


if __name__ == '__main__':
    M = '4'
    F = '7'

    print answer(M, F)