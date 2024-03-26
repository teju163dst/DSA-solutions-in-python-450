arr = [1, 2, 3, 4, 5]
n = len(arr)
 
# store last element in a temporary variable
temp = arr[n-1]
 
# shift each element one position to the right
for i in range(n-1, 0, -1):
    arr[i] = arr[i-1]
 
# move the temporary variable to the first position
arr[0] = temp
print(arr)
