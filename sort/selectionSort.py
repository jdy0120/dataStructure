# Selection Sort

def selectionSort(unOrdered):
    ordered = unOrdered[:]
    for x in range(len(ordered)-1):
        for y in range(x+1, len(ordered)):
            if (ordered[x] > ordered[y]):
                ordered[x], ordered[y] = ordered[y], ordered[x]

    return ordered
