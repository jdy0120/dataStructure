# -*- coding: utf-8 -*-
# Selection Sort 최선: O(N^2) 최악: O(N^2)

def selectionSort(unOrdered):
    ordered = unOrdered[:]
    for x in range(len(ordered)-1):
        for y in range(x+1, len(ordered)):
            if (ordered[x] > ordered[y]):
                ordered[x], ordered[y] = ordered[y], ordered[x]

    return ordered
