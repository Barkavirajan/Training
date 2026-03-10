#1. Given two sorted arrays, design an algorithm to find the median in O(log(min(n, m))) time.
def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    x, y = len(nums1), len(nums2)
    low, high = 0, x

    while low <= high:
        partitionX = (low + high) // 2
        partitionY = (x + y + 1) // 2 - partitionX

        maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX-1]
        minRightX = float('inf') if partitionX == x else nums1[partitionX]

        maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY-1]
        minRightY = float('inf') if partitionY == y else nums2[partitionY]

        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            if (x + y) % 2 == 0:
                return (max(maxLeftX,maxLeftY)+min(minRightX,minRightY))/2
            else:
                return max(maxLeftX,maxLeftY)

        elif maxLeftX > minRightY:
            high = partitionX - 1
        else:
            low = partitionX + 1
print(findMedianSortedArrays([1, 3], [2])) 

#2.You have n sorted files of different sizes. Find the minimum cost to merge them into one file using an optimal strategy (similar to Huffman coding).
import heapq

def min_merge_cost(files):
    heapq.heapify(files)
    cost = 0

    while len(files) > 1:
        a = heapq.heappop(files)
        b = heapq.heappop(files)

        merge = a + b
        cost += merge

        heapq.heappush(files, merge)

    return cost

files = [20,30,10,5]
print(min_merge_cost(files))

#3.Given dimensions of matrices, find the optimal order to multiply them to minimize the total number of scalar multiplications.
import sys
def matrix_chain_order(p):
    n = len(p)
    dp = [[0]*n for _ in range(n)]
    for L in range(2,n):
        for i in range(1,n-L+1):
            j = i+L-1
            dp[i][j] = sys.maxsize
            for k in range(i,j):
                q = dp[i][k] + dp[k+1][j] + p[i-1]*p[k]*p[j]
                dp[i][j] = min(dp[i][j],q)
    return dp[1][n-1]

arr = [40,20,30,10,30]
print(matrix_chain_order(arr))