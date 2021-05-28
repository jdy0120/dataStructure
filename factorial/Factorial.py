def FactorialBottomUp(n):
    answer = 1
    for x in range(1, n+1):
        answer *= x
    return answer


def FactorialTopDown(n, memoization):
    if memoization[n] != -1:
        return memoization[n]
    if n == 1:
        return 1
    memoization[n] = FactorialTopDown(n-1, memoization)*n
    return memoization[n]
