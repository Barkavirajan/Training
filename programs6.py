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

#4.Given a network with capacities and demands, compute the maximum flow from source to sink using an optimal algorithm (e.g., Ford-Fulkerson or Edmonds-Karp).
from collections import deque

def bfs(capacity, source, sink, parent):
    visited = [False]*len(capacity)
    queue = deque([source])
    visited[source] = True
    while queue:
        u = queue.popleft()
        for v in range(len(capacity)):
            if not visited[v] and capacity[u][v] > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u
    return visited[sink]

def max_flow(capacity, source, sink):
    parent = [-1]*len(capacity)
    flow = 0
    while bfs(capacity, source, sink, parent):
        path_flow = float("inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, capacity[parent[s]][s])
            s = parent[s]
        flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            capacity[u][v] -= path_flow
            capacity[v][u] += path_flow
            v = parent[v]
    return flow

#5.You are given n jobs with processing times and deadlines. Schedule them to minimize the total completion time or lateness.
jobs = [(3,4),(2,2),(1,3)]
jobs.sort(key=lambda x:x[1])
time = 0
for p,d in jobs:
    time += p
    print("Completion:",time,"Deadline:",d)

#6. You have 5 jobs and 2 machines. Each job has a processing time and must be assigned to one machine.Design an optimization approach to minimize the makespan (total completion time) using integer programming.
import pulp

p=[2,4,6,3,5]
m=range(2)
j=range(len(p))
prob=pulp.LpProblem("M",pulp.LpMinimize)
x=pulp.LpVariable.dicts("x",(j,m),0,1,cat="Binary")
T=pulp.LpVariable("T",0)
prob+=T
for i in j: prob+=sum(x[i][k] for k in m)==1
for k in m: prob+=sum(p[i]*x[i][k] for i in j)<=T
prob.solve()
print(T.value(),{i:k for i in j for k in m if x[i][k].value()==1})

#7. Write a function to find the maximum product of a contiguous subarray in an array of integers (including negatives and zeros).
#Example: Input: [2, 3, -2, 4] Output: 6 (subarray [2, 3])

def maxProduct(nums):
    max_prod = nums[0]
    min_prod = nums[0]
    result = nums[0]
    for i in range(1,len(nums)):
        if nums[i] < 0:
            max_prod, min_prod = min_prod, max_prod
        max_prod = max(nums[i], max_prod*nums[i])
        min_prod = min(nums[i], min_prod*nums[i])
        result = max(result, max_prod)
    return result
print(maxProduct([2,3,-2,4]))

#8.You manage a team of k members and m projects, each with stress impact scores.
#Question: Assign projects to team members so that maximum individual stress is minimized. (Hint: Similar to load balancing or min-max optimization.)
import heapq

def minimize_stress(projects, k):
    workers = [0]*k
    heapq.heapify(workers)
    for p in projects:
        load = heapq.heappop(workers)
        heapq.heappush(workers, load+p)
    return max(workers)
projects = [3,7,2,6,4]
print(minimize_stress(projects,3))

#9.Given a singly linked list, determine if it contains a cycle using Floyd’s Tortoise and Hare algorithm.
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
def hasCycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

#10. Write a program that: Takes an integer n. Returns its prime factorization in ascending order.
#Example: Input: n = 84 → Output: 2^2 × 3 × 7
def prime_factors(n):
    i = 2
    factors = {}
    while i*i <= n:
        while n % i == 0:
            factors[i] = factors.get(i,0)+1
            n //= i
        i += 1
    if n > 1:
        factors[n] = 1
    return factors
print(prime_factors(84))

#11.From a group of 12 players, you need to select a team of 5 players.
#Question:
#How many ways can you choose the team?
#How many ways if one specific player must be included?

import math
# choose 5 from 12
print(math.comb(12,5))

# specific player included
print(math.comb(11,4))

#12.1. A password consists of 6 characters, each can be a digit (0–9) or an uppercase letter (A–Z).
#Question:
#How many possible passwords exist if:
#Characters can repeat?
#Characters cannot repeat?

print(36**6) #repeat
import math
print(math.perm(36,6)) #no repeat

