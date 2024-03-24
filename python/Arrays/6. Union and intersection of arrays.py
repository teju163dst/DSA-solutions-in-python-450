# Here I am using Two pointer approach
# steps 
   1. use two index variables i and j, initial values i = 0, j = 0 
   2. If arr1[i] is smaller than arr2[j] then print arr1[i] and increment i. 
   3. If arr1[i] is greater than arr2[j] then print arr2[j] and increment j. 
   4. If both are same then print any of them and increment both i and j.
   5. Print remaining elements of the larger array.

 def printunion(arr1,arr2,m,n)
     i,j=0,0
     while i<m and j<n:
       if arr1[i]<arr2[j]:
         print(arr1[i],end="")
         i+=1
       elif arr2[j]<arr1[i]:
         print(arr2[j],end="")
         j+=1
       else:
         print(arr2[j],end="")
         j+=1
         i+=1
         
# Print remaining elements of the larger array
    while i < m:
        print(arr1[i],end=" ")
        i += 1
 
    while j < n:
        print(arr2[j],end=" ")
        j += 1    



# Intersection of two sorted arrays using 2 pointer 
Use two index variables i and j, initial values i = 0, j = 0 
If arr1[i] is smaller than arr2[j] then increment i. 
If arr1[i] is greater than arr2[j] then increment j. 
If both are same then print any of them and increment both i and j.

def printIntersection(arr1, arr2, m, n):
    i, j = 0, 0
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j+= 1
        else:
            print(arr2[j],end=" ")
            j += 1
            i += 1
 


