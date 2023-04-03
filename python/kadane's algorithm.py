# Given an array arr[] of size N. The task is to find the sum of the contiguous subarray within a arr[] with the largest sum. 
# For each number calculate max subarray sum ending with that number as either number alone(if previous sum was -) 
# or number+previous sum(if previous sum is +)
# anytime you get - prefix remove as you want highest sum 

class Solution:
    def maxSubArraySum(self,arr,N):
        n = N
        max_so_far = -1e8
        max_ending_here = 0
    
        for i in range(0, n):
            max_ending_here = max_ending_here + arr[i]
            if (max_so_far < max_ending_here):
                max_so_far = max_ending_here
     
            if max_ending_here < 0:
                max_ending_here = 0
        return max_so_far

# Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends


