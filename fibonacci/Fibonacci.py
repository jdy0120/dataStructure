# -*- coding:utf-8 -*-
import sys
from timeit import default_timer as timer
from datetime import timedelta
sys.setrecursionlimit(100000)


def fibonacciTopDown(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if memoization[n] != -1:
        return memoization[n]
    memoization[n] = fibonacciTopDown(n-1) + fibonacciTopDown(n-2)
    return memoization[n]


def fibonacciBottomUp(n):
    answer = 0
    first = 0
    second = 1
    for x in range(1, n):
        answer = first+second
        first = second
        second = answer
    return answer


length = int(input())
memoization = [-1]*length
start = timer()
print(fibonacciTopDown(length-1))
end = timer()
print('fibonacciTopDown 걸린 시간 >>> {0}'.format(timedelta(seconds=end-start)))

start = timer()
print(fibonacciBottomUp(length-1))
end = timer()
print('fibonacciBottomUp 걸린 시간 >>> {0}'.format(timedelta(seconds=end-start)))
