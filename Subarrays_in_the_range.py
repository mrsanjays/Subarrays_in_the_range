"""
Given an array A of length N, return the subarray from B to C.
"""
class Solution:
    def Subarrays_in_range(self,array,l,r):
        for i in range(l,r+1):
            print(array[i],end=" ")

if __name__ == '__main__':
    array=list(map(int,input().split()))
    b,c=map(int,input().split())
    Solution().Subarrays_in_range(array,b,c)