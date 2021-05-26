# -*- coding: utf-8 -*-
# Merge Sort 최선: O(NlogN) 최악: O(NlogN)

def mergeSort(unOrdered):
    if len(unOrdered) == 1 or len(unOrdered) == 0:
        return unOrdered

    leftArray = unOrdered[:len(unOrdered)//2]
    rightArray = unOrdered[len(unOrdered)//2:]

    leftMerge = mergeSort(leftArray)
    rightMerge = mergeSort(rightArray)

    ordered = []
    while (leftMerge or rightMerge):
        if not leftMerge:
            ordered.extend(rightMerge)
            break
        if not rightMerge:
            ordered.extend(leftMerge)
            break

        if (leftMerge[0] < rightMerge[0]):
            ordered.append(leftMerge[0])
            leftMerge = leftMerge[1:]
        else:
            ordered.append(rightMerge[0])
            rightMerge = rightMerge[1:]
    return ordered
