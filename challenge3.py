dp = [ [-1]*201 for i in range(201) ]
def f(n,s):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if dp[n][s] > 0:
        return dp[n][s]
    dp[n][s] = f(n-1,s+1) + f(n-s-1, s+1)
    return dp[n][s]

def answer(n):
    return f(n-1,1)-1


print answer(200)