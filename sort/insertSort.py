# -*- coding: utf-8 -*-
# insert sort 최선:O(N) 최악: O(N^2)

def insertSort(unordered):
    ordered = unordered[:]
    for x in range(len(ordered)):
        key = ordered[x]
        y = x-1
        while y >= 0 and ordered[y] > key:
            ordered[y+1] = ordered[y]
            y -= 1
        ordered[y+1] = key
    return ordered
