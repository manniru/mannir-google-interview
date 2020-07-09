def answer(l):
    res = [i for i in l if i % 3 == 0]
    l = [i for i in l if i % 3 != 0]
    l.sort(reverse=True)

    partial = []
    start = 0

    for start, _ in enumerate(l):
        end = len(l)
        while end >= start:
            window = l[0:start] + l[end:len(l)]
            the_sum = sum(window)
            if the_sum % 3 == 0:
		if len(window) > len(partial) or (len(window) == len(partial) and the_sum > sum(partial)):
                    partial = window
            end -= 1
    res = res + partial
    res.sort(reverse=True)
    res = int(''.join(str(d) for d in res) or 0)
    return res