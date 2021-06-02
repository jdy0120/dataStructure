# -*- coding: utf-8 -*-
# Selection Sort 최선: O(N^2) 최악: O(N^2)

def selectionSort(unOrdered):
    ordered = unOrdered[:]
    for x in range(len(ordered)-1):
        minimum = -1
        where = -1
        for y in range(x+1, len(ordered)):
            if minimum == -1 or minimum > ordered[y]:
                minimum = ordered[y]
                where = y
        if minimum < ordered[x]:
            ordered[x], ordered[where] = ordered[where], ordered[x]

    return ordered
