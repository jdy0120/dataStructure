# -*- coding: utf-8 -*-
# Quick Sort 최선: O(NlogN) 최악: O(N^2)

def quickSort(unordered):
    if len(unordered) == 0:
        return unordered

    pivot = unordered[0]
    small = []
    big = []

    for x in unordered[1:]:
        if pivot > x:
            small.append(x)
        else:
            big.append(x)

    left = quickSort(small)
    right = quickSort(big)

    return left + [pivot] + right
