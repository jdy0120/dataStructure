# Quick Sort

def quickSort(unordered):
    if not unordered:
        return []
    pivot = unordered[0]
    smaller = []
    bigger = []

    for x in range(1, len(unordered)):
        if unordered[x] < pivot:
            smaller.append(unordered[x])
        else:
            bigger.append(unordered[x])

    left = quickSort(smaller)
    right = quickSort(bigger)
    return left+[pivot]+right
