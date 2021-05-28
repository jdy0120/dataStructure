# -*- coding:utf-8 -*-
from timeit import default_timer as timer
from datetime import timedelta
from Factorial import FactorialTopDown, FactorialBottomUp
import sys

sys.setrecursionlimit(100000)

print('n 팩토리얼: ')
n = int(input())
memoization = [-1]*(n+1)

start = timer()
print(FactorialTopDown(n, memoization))
end = timer()
print('TopDown 걸린 시간 >>>> {0}'.format(timedelta(seconds=end-start)))

start = timer()
print(FactorialBottomUp(n))
end = timer()
print('BottomUp 걸린 시간 >>>> {0}'.format(timedelta(seconds=end-start)))
