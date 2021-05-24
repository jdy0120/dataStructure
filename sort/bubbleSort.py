# Bubble Sort 최선: O(N^2) 최악: O(N^2)

def bubbleSort(unOrdered):
    ordered = unOrdered[:]
    for x in range(len(ordered)-1, 0, -1):
        for y in range(x):
            if (ordered[y] > ordered[y+1]):
                ordered[y], ordered[y+1] = ordered[y+1], ordered[y]

    return ordered
