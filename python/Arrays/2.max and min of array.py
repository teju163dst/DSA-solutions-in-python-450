## Given an array of size N. The task is to find the maximum and the minimum element of the array
## using the minimum number of comparisons.

## 1.Initialize an array.
## 2.Sort the array in ascending order.
## 3. The first element of the array will be the minimum element.
## 4. The last element of the array will be the maximum element.
## 5. Print the minimum and maximum element.


def getMinMax(arr):
    arr.sort()
    minmax = {"min": arr[0], "max": arr[-1]}
    return minmax

arr = [1000, 11, 445, 1, 330, 3000]
minmax = getMinMax(arr)

print("Minimum element is", minmax["min"])
print("Maximum element is", minmax["max"])