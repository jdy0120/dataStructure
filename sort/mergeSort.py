# Merge Sort 최선: O(NlogN) 최악: O(NlogN)

def mergeSort(unOrderedLeft, unOrderedRight=False):
    if len(unOrderedLeft) == 0:
        return unOrderedRight
    if unOrderedRight and len(unOrderedRight) == 0:
        return unOrderedLeft

    leftArray = mergeSort(unOrderedLeft[:len(
        unOrderedLeft)//2], unOrderedLeft[len(unOrderedLeft)//2:])

    if (unOrderedRight == False):
        rightArray = []
    else:
        rightArray = mergeSort(unOrderedRight[:len(
            unOrderedRight)//2], unOrderedRight[len(unOrderedRight)//2:])

    ordered = []
    while (leftArray or rightArray):
        if not leftArray:
            ordered.extend(rightArray)
            break
        if not rightArray:
            ordered.extend(leftArray)
            break

        if (leftArray[0] < rightArray[0]):
            ordered.append(leftArray[0])
            leftArray = leftArray[1:]
        else:
            ordered.append(rightArray[0])
            rightArray = rightArray[1:]
    return ordered
