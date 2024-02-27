# Implementation of Quicksort (recursive algorithm)
def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


def partition(A, start, end):
    pivot = A[len(A) - 1]
    i = start - 1

    for j in range(start, end - 1):
        if A[j] < pivot:
            i += 1
            swap(A, i, j)
    # Place pivot in correct location
    swap(A, i + 1, end)
    return i + 1


def quicksort(A, start, end):
    # Base Case
    if end <= start:
        return

    # Retrieve pivot index
    pivot = partition(A, start, end)

    # Left Subarray
    quicksort(A, start, pivot - 1)
    # Right Subarray
    quicksort(A, pivot + 1, end)

    return A


input_list = [3, 5, 1, 7, 4]

print(quicksort(input_list, 0, len(input_list) - 1))

# OUTPUT: [1, 3, 4, 5, 7]
