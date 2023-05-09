# Given an array and a number K where K is smaller than the size of the array. Find the
# K’th smallest element in the given array. Given that all array elements are distinct.

# Sort the input array in the increasing order
# Return the element at the K-1 index (0 – Based indexing) in the sorted array
#
def kthSmallest(arr, N, K):
    # Sort the given array
    arr.sort()

    # Return k'th element in the
    # sorted array
    return arr[K - 1]


# Driver code
if __name__ == '__main__':
    arr = [12, 3, 5, 7, 19]
    N = len(arr)
    K = 2

    # Function call
    print("K'th smallest element is",
          kthSmallest(arr, N, K))
#

def kLargest(arr, k):
    # Sort the given array arr in reverse
    # order.
    arr.sort(reverse=True)
    # Print the first kth largest elements
    for i in range(k):
        print(arr[i], end=" ")


# Driver code
arr = [1, 23, 12, 9, 30, 2, 50]
# n = len(arr)
k = 1
kLargest(arr, k)