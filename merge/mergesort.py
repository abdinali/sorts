# Implementation of Merge Sort

def mergesort(A):
    # Base Case
    if len(A) == 1:
        return

    mid = (len(A)) // 2

    # Left Subarray
    leftA = []
    for i in range(0, mid):
        leftA.append(A[i])

    # Right Subarray
    rightA = []
    for i in range(mid, len(A)):
        rightA.append(A[i])

    mergesort(leftA)
    mergesort(rightA)

    merge(A, leftA, rightA)

    return A


def merge(A, leftA, rightA):
    i = 0
    j = 0
    k = 0

    while i < len(leftA) and j < len(rightA):
        if leftA[i] <= rightA[j]:
            A[k] = leftA[i]
            i = i + 1
        else:
            A[k] = rightA[j]
            j = j + 1
        k = k + 1

    # Leftovers
    while i < len(leftA):
        A[k] = leftA[i]
        i += 1
        k += 1

    while j < len(rightA):
        A[k] = rightA[j]
        j += 1
        k += 1

    return A


input_list = [4, 9, 1, 2, 5, 6, 3]

print(mergesort(input_list))

# OUTPUT: [1, 2, 3, 4, 5, 6, 9]
