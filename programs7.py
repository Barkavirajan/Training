#1.Sequence generation:
#Create a sequence of length n where:
#Odd positions contain increasing positive integers
#Even positions contain decreasing negative integers

#2.Cumulative sums concepts:
#Given an array of integers, build a prefix sum array where each element at index i is the sum of all elements from 0 to i.
#Example: Input: [2, 4, 6, 8]

#3.Interval overlap concepts:
#Given a list of intervals, merge all overlapping intervals and return a new list of non-overlapping intervals sorted by start time.
#Example: Input: [(1, 3), (2, 6), (8, 10), (9, 12)]

#4.Preprocessing:
#A dataset contains columns like Gender (Male, Female) and City (New York, Paris, Tokyo).
#Task: Implement One-Hot Encoding and Label Encoding.

#5.Divisor concepts:
#Given a number n, find the count of its proper divisors (divisors excluding the number itself).
#Example: Input: n = 28 Output: 5 (divisors: 1, 2, 4, 7, 14)
#For a given integer n, find the largest divisor less than n (excluding n itself).  these are the python dsa question so can you explain these questions clearly with output detailly 

#1.
def generate_sequence(n):
    result = []
    positive = 1
    negative = -1
    for i in range(1, n + 1):
        if i % 2 != 0:   
            result.append(positive)
            positive += 1
        else:            
            result.append(negative)
            negative -= 1
    return result
print(generate_sequence(6))

#2.
def prefix_sum(arr):
    prefix = []
    current_sum = 0
    for num in arr:
        current_sum += num
        prefix.append(current_sum)
    return prefix
print(prefix_sum([2, 4, 6, 8]))

#3.
def merge_intervals(intervals):
    intervals.sort()   
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:           
            merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))
    return merged
intervals = [(1, 3), (2, 6), (8, 10), (9, 12)]
print(merge_intervals(intervals))

#4.
from sklearn.preprocessing import LabelEncoder
gender = ["Male", "Female", "Male"]
city = ["New York", "Paris", "Tokyo"]
le_gender = LabelEncoder()
le_city = LabelEncoder()
print("Gender Label Encoding:", le_gender.fit_transform(gender))
print("City Label Encoding:", le_city.fit_transform(city))

import pandas as pd
data = pd.DataFrame({
    "Gender": ["Male", "Female", "Male"],
    "City": ["New York", "Paris", "Tokyo"]
})
encoded = pd.get_dummies(data)
print(encoded)

#5.
def count_proper_divisors(n):
    count = 0
    for i in range(1, n):
        if n % i == 0:
            count += 1
    return count
print(count_proper_divisors(28))

def largest_proper_divisor(n):
    for i in range(n-1, 0, -1):
        if n % i == 0:
            return i
print(largest_proper_divisor(28))
