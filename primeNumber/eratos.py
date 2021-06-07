# -*- coding: utf-8 -*-
def eratos(endNumber):
    prime = [True]*(endNumber+1)
    prime[0] = prime[1] = False
    for x in range(2, endNumber):
        if prime[x]:
            y = x+x
            while y <= endNumber:
                prime[y] = False
                y += x
    answer = [x for x in range(1, endNumber+1)]
    return filter(lambda x: prime[x], answer)


print('숫자 몇까지 소수를 구하겠습니까?')
n = int(input())
print(eratos(n))
