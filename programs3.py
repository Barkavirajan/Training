#1. Given text, return sorted unique words ignoring case 
#2. Merge two inventory dicts by summing qualities of same keys
#3.return list of(elements, count) in order of first appearance  
#4.given a dict and target value, return all keys that map to that value
#5. convert list with duplicates into list of unique element while preserving no order
#6.Count the frequency of each word in a given paragraph and return a dictionary sorted by frequency
#7. From a dictionary of employee salaries, find the employee with the highest salary
#8. given a list of tuples (item, category ) create a dict grouping items under their categories
#9.Write fib(n) that computer,the nth Fibonacci number efficiently with memoization. Provide two versions Using a dictionary cache inside the function Using a custom @memoize decorator that caches by arguments
#10. Write a function normalize_name(s: str) -> str that Strips extra whitespace Converts to title case Collapses multiple spaces into single spaces If s is empty or contains only spaces, retun "".

#1.
def sorted_uniquewords(text):
    words = set(text.lower().split())
    return sorted(words)
text = "This is a sample text with Sample words and words"
print(sorted_uniquewords(text))

#2.
def merge_inventory(inv1, inv2):
    merged = inv1.copy()
    for item, qty in inv2.items():
        merged[item] = merged.get(item, 0) + qty
    return merged
inv1 = {'apple': 10, 'banana': 5}
inv2 = {'banana': 3, 'orange': 7}   
print(merge_inventory(inv1, inv2))

#3.
def count_in_order(lst):
    seen = {}
    for x in lst:
        seen[x] = seen.get(x, 0) + 1
    return list(seen.items())
lst = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
print(count_in_order(lst))

#4.
def keys_for_value(d, target):
    return [k for k, v in d.items() if v == target]
d = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
target = 1  
print(keys_for_value(d, target))

#5.
def unique_elements(lst):
    return list(set(lst))
lst = [1, 2, 2, 3, 4, 4, 5]
print(unique_elements(lst))

#6.
def word_frequency(text):
    words = text.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
text = "This is a test this is only a test"
print(word_frequency(text))

#7.
def highest_salary(employee):
    return max(employee, key=employee.get)
employee = {'Alice': 70000, 'Bob': 80000, 'Charlie': 60000}
print(highest_salary(employee))

#8.
def group_bycategory(pairs):
    freq = {}
    for item, category in pairs:
        if category not in freq:
            freq[category] = []
        freq[category].append(item)
    return freq
pairs = [('apple', 'fruit'), ('carrot', 'vegetable'), ('banana', 'fruit')]
print(group_bycategory(pairs))

#9.Version 1: Dictionary cache
def fib(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

#9. Version 2: Decorator memoization
def memoize(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper

#10.
def normalize_name(s):
    s = ' '.join(s.split())
    return s.title() if s else ""
s = "   john    doe   "
print(normalize_name(s))


