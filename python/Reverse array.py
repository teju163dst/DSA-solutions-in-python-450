# Given an array (or string), the task is to reverse the array/string.

# Input  : arr[] = {1, 2, 3}
# Output : arr[] = {3, 2, 1}

# 1 Initialize start and end indexes as start = 0, end = n-1 
# 2 Swap arr[start] with arr[end] 
# 3 Recursively call reverse for rest of the array.

def reverseList(A, start, end):
    if start >= end:
        return
    A[start], A[end] = A[end], A[start]
    reverseList(A, start+1, end-1)
 
# Driver function to test above function
A = [1, 2, 3, 4, 5, 6]
print(A)
reverseList(A, 0, 5)
print("Reversed list is")
print(A)