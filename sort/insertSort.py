# -*- coding: utf-8 -*-
# insert sort 최선:O(N) 최악: O(N^2)

def insertSort(unOrdered):
    ordered = unOrdered[:]
    for x in range(1, len(ordered)):
        for y in range(x-1, -1, -1):
            if (ordered[y+1] < ordered[y]):
                ordered[y], ordered[y+1] = ordered[y+1], ordered[y]
            else:
                break
    return ordered
