# -*- coding: utf-8 -*-

from GCF import GCF
from LCM import LCM

print('첫번째 숫자를 입력하세요: ')
a = int(input())
print('두번째 숫자를 입력하세요: ')
b = int(input())
print('{0},{1}의 최대공약수 : {2}'.format(a, b, GCF(a, b)))
print('{0},{1}의 최소공배수 : {2}'.format(a, b, LCM(a, b)))
