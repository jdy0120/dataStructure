# -*- coding: utf-8 -*-
# Merge Sort 최선: O(NlogN) 최악: O(NlogN)

def mergeSort(unordered):
    if len(unordered) == 1 or len(unordered) == 0:
        return unordered
    leftArray = unordered[:len(unordered)//2]
    rightArray = unordered[len(unordered)//2:]

    leftMerge = mergeSort(leftArray)
    rightMerge = mergeSort(rightArray)

    ordered = []
    while leftMerge or rightMerge:
        if not leftMerge:
            ordered.extend(rightMerge)
            break
        if not rightMerge:
            ordered.extend(leftMerge)
            break

        if leftMerge[0] > rightMerge[0]:
            ordered.append(rightMerge[0])
            rightMerge = rightMerge[1:]
        else:
            ordered.append(leftMerge[0])
            leftMerge = leftMerge[1:]
    return ordered
