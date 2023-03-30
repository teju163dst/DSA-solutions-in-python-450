# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects 
# of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# we have to use bucket sort where 0,1 and 2 are individual buckets

# The problem was posed with three colors, here `0′, `1′ and `2′. The array is divided into four sections: 
# arr[1] to arr[low – 1]
# arr[low] to arr[mid – 1]
# arr[mid] to arr[high – 1]
# arr[high] to arr[n]
# If the ith element is 0 then swap the element to the low range.
# Similarly, if the element is 1 then keep it as it is.
# If the element is 2 then swap it with an element in high range.

def sort012(a,arr_size):
    lo=0
    mid=arr_size-1
    hi=0
    # Iterate till all elements are sorted
    while mid<=hi:
        # If the element is 0
        if a[mid]==0:
            a[lo],a[mid]=a[mid],a[lo]
            lo=lo+1
            mid=mid+1
        # If the element is 1
        elif a[mid]==1:
            mid=mid+1
             # If the element is 2
        else:
            a[mid], a[hi] = a[hi], a[mid]
            hi = hi - 1
    return a
  
# Function to print array
  
  
def printArray(a):
    for k in a:
        print(k, end=' ')
  
  
# Driver Program
arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
arr_size = len(arr)
arr = sort012(arr, arr_size)
printArray(arr)
    
