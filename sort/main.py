# -*- coding: utf-8 -*-

import random
from timeit import default_timer as timer
from datetime import timedelta
from selectionSort import selectionSort
from insertSort import insertSort
from bubbleSort import bubbleSort
from mergeSort import mergeSort
from quickSort import quickSort


def getTimeAndList(division, dataList):
    start = timer()
    if (division == 'selectionSort'):
        print('selectionSort >>> {0}'.format(selectionSort(dataList)))
    elif(division == 'insertSort'):
        print('insertSort >>> {0}'.format(insertSort(dataList)))
    elif(division == 'bubbleSort'):
        print('bubbleSort >>> {0}'.format(bubbleSort(dataList)))
    elif(division == 'mergeSort'):
        print('mergeSort >>> {0}'.format(mergeSort(dataList)))
    elif(division == 'quickSort'):
        print('quickSort >>> {0}'.format(quickSort(dataList)))
    else:
        print('python 내부 sort함수 사용 >>> {0}'.format(sorted(dataList)))
    end = timer()
    print('{0} 걸린 시간 >>>> {1}'.format(division, timedelta(seconds=end-start)))


print('배열의 길이를 적어주세요: ')
n = int(input())
dataList = list(range(0, n))
print('배열은 {0} 입니다.'.format(dataList))

random.shuffle(dataList)
print('섞인 배열은 {0} 입니다.'.format(dataList))


getTimeAndList('selectionSort', dataList)
getTimeAndList('insertSort', dataList)
getTimeAndList('bubbleSort', dataList)
getTimeAndList('mergeSort', dataList)
getTimeAndList('quickSort', dataList)
getTimeAndList('내부 sort', dataList)
