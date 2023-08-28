import random


# Insertion sort & returns number of swaps
def insertionSort(array):
    num_swaps = 0
    for i in range(1, len(array)):
        key = array[i]

        j = i-1
        while j >= 0 and key < array[j]:
            num_swaps += 1
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return num_swaps


# Bubble sort & return number of swaps
def bubbleSort(array):
    arrLen = len(array)
    swaps = 0

    for i in range(1, len(array)):
        for j in range(0, arrLen-i):
            if array[j] > array[j+1]:
                swaps += 1
                array[j], array[j+1] = array[j+1], array[j]
    return swaps


# Merge sort
def mergeSort(array):
    if len(array) > 1:
        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]
        mergeSort(left)
        mergeSort(right)
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    return


def testInsertionSort(array):
    testArr = array.copy()

    print("-- Insertion Sort --")
    print(f"Prev test array: {testArr}")
    swaps = insertionSort(testArr)
    print(f"Sorted test array: {testArr}")
    print(f"Num swaps: {swaps} \n")



def testBubbleSort(array):
    testArr = array.copy()

    print("-- Bubble Sort --")
    print(f"Prev test array: {testArr}")
    swaps = bubbleSort(testArr)
    print(f"Sorted test array: {testArr}")
    print(f"Num swaps: {swaps} \n")


def testMergeSort(array):
    testArr = array.copy()

    print("-- Merge Sort --")
    print(f"Prev test array: {testArr}")
    mergeSort(testArr)
    print(f"Sorted test array: {testArr} \n")
    # print(f"Num swaps: {swaps}")


# Test array to be sorted
testArray = [1, 2, 55, 43, 4, 66, 41, 531, 0, 11, 41, 98]
# randTestArray = [random.randint(1, 999) for _ in range(100)]

testInsertionSort(testArray)
testBubbleSort(testArray)
testMergeSort(testArray)
