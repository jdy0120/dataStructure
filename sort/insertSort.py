# -*- coding: utf-8 -*-
# insert sort 최선:O(N) 최악: O(N^2)

def insertSort(unordered):
    ordered = unordered[:]
    for x in range(1, len(ordered)):
        y = x - 1
        key = ordered[x]
        while ordered[y] > key and y >= 0:
            ordered[y+1] = ordered[y]
            y = y - 1
        ordered[y+1] = key
    return ordered
