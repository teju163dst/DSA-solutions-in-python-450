# An array contains both positive and negative numbers in random order. Rearrange the array elements
# so that all negative numbers appear before all positive numbers.
# We will divide the array into three partitions with the help of two pointers, low and high.
# ar[1…low-1] negative integers
# ar[low…high] unknown
# ar[high+1…N] positive integers
# we explore the array with the help of low pointer, shrinking the unknown partition, and moving elements
# to their correct partition in the process. We do this until we have explored all the elements,
# and size of the unknown partition shrinks to zero.

# Using Dutch National Flag Algorithm.
def reArrange(arr, n):
    low, high = 0, n - 1
    while (low < high):
        if (arr[low] < 0):
            low += 1
        elif (arr[high] > 0):
            high -= 1
        else:
            arr[low], arr[high] = arr[high], arr[low]


def displayArray(arr, n):
    for i in range(n):
        print(arr[i], end=" ")

    print('')


# driver code
# Data
arr = [1, 2, -4, -5, 2, -7, 3, 2, -6, -8, -9, 3, 2, 1]
n = len(arr)
reArrange(arr, n)
displayArray(arr, n)