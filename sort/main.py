# -*- coding:utf-8 -*-
import random
from selectionSort import selectionSort
from insertSort import insertSort
from bubbleSort import bubbleSort
from mergeSort import mergeSort
from quickSort import quickSort

print('배열의 길이를 적어주세요: ')
n = int(input())
dataList = list(range(0, n))
print('배열은 {0} 입니다.'.format(dataList))

random.shuffle(dataList)
print('섞인 배열은 {0} 입니다.'.format(dataList))

print('selectionSort >>> {0}'.format(selectionSort(dataList)))
print('insertSort >>> {0}'.format(insertSort(dataList)))
print('bubbleSort >>> {0}'.format(bubbleSort(dataList)))
print('mergeSort >>> {0}'.format(mergeSort(dataList)))
print('quickSort >>> {0}'.format(quickSort(dataList)))
print('python 내부 sort함수 사용 >>> {0}'.format(sorted(dataList)))
