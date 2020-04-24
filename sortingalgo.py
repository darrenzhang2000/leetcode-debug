def bubbleSort(arr):
    isSorted = False
    counter = 0
    while not isSorted:
        isSorted = True
        for i in range(len(arr) - 1 - counter):
            if arr[i] > arr[i + 1]:
                swap(i, i + 1 , arr)
                isSorted = False
            counter += 1
        return arr
def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]


def selectionSort(arr):
    currentIdx = 0
    while currentIdx < len(arr) - 1:
        smallest = currentIdx
        for i in range(currentIdx + 1, len(arr)):
            if arr[smallestIdx] > arr[i]:
                smallestIdx = i
        swap(currentIdx, smallestIdx, arr)
        currentIdx += 1
    return arr

def insertionSort(arr):
    for i in range(1, len(arr)):
        j = 1
        while j > 0 and arr[j] < arr[j - 1]:
            swap(j, j - 1, arr)
            j -= 1
        return arr

