arr = [5, 8, 4, 3, 1, 9, 7, 16, 2, 10]

def swap(arr, i1, i2):
    temp = arr[i1]
    arr[i1] = arr[i2]
    arr[i2] = temp

def selectionSort(arr):
    for i in range(len(arr)):
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        swap(arr, minIndex, i)

selectionSort(arr)

print(arr)
# Sorted Output: [1, 2, 3, 4, 5, 7, 8, 9, 10, 16]