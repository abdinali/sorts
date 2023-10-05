arr = [3, 7, 9, 2, 4, 6, 11, 5]

def bubbleSort(arr):
    for i in range(len(arr)): 
        for j in range(1, len(arr) - i):
            if arr[j] < arr[j - 1]:
                temp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = temp

bubbleSort(arr)

print(arr)
# Sorted Output: [2, 3, 4, 5, 6, 7, 9, 11]