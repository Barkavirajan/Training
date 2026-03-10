#1.Implement python functions (hash,op="sum") support colon op = "sum" -> sum of numbers op = "avg" -> average (float), op ="max" -> maximum. if no number provided return None
#2. write make_counter(start=0) that return a function counter() which, each time it is called, increments and returns next value(1,2,3...starting from start+1).
#3. create check_strength(pwd):str, min_length = 8 )-> dict return in colon { "Length_" colon bool,"has upper" colon boolean, "has lower" colon boolean, "has digit" colon boolean, score colon int has sum of two values} special character or anything not alpha numeric
#4. you are give a list of products name inconsist and extra spaces colon names = [" alpha "," beta unit "," eAmMa MODULE " ] use map with lambda to strip spaces and convert to Tittle Case(example " alphacase")
#5.create a Price Update Pipeline (map -> filter -> reduce) given n list of product, apply a 10% discount, keep only items >= dollar 200 after discount and compute the final bill total
#6. calculate weighted score aggregation using reduce when given list of scores and weights    
#7. write a generator function count_up_to(n) that yields numbers from 1 to n.      
#8. write a generator function fib() that yields fib numbers
#9. use itertools.islice() to make the first 5 elements if generator multiples of 5
#10. use a generator  expression compute and sum of squares of number from 1 to 100

#1.
def calc(nums, op="sum"):
    if not nums:
        return None    
    if op == "sum":
        return sum(nums)
    elif op == "avg":
        return sum(nums) / len(nums)
    elif op == "max":
        return max(nums)
    else:
        raise ValueError("Unsupported operation")
print(calc([1, 2, 3, 4], "sum"))  
print(calc([1, 2, 3, 4], "avg"))  
print(calc([1, 2, 3, 4], "max"))  
print(calc([], "sum")) 

#2.
def make_counter(start=0):
    count = start    
    def counter():
        nonlocal count
        count += 1
        return count    
    return counter
c = make_counter(5)
print(c())  
print(c())  
print(c())

#3.
def check_strength(pwd, min_length=8):
    is_upper = False
    is_lower = False
    is_digit = False
    score = 0
    if len(pwd) >= min_length:
        score += 1
        is_upper = any(c.isupper() for c in pwd)
        is_lower = any(c.islower() for c in pwd)
        is_digit = any(c.isdigit() for c in pwd)
        if is_upper:
            score += 1
        if is_lower:
            score += 1
        if is_digit:
            score += 1
    return {
        "Length": len(pwd) >= min_length,
        "has upper": is_upper,
        "has lower": is_lower,
        "has digit": is_digit,
        "score": score
    }
print(check_strength("MyPass123"))

#4.
names = [" alpha ", " beta unit ", " eAmMa MODULE "]
clean_names = list(map(lambda x: x.strip().title(), names))
print(clean_names)

#5.
from functools import reduce
prices = [150, 250, 300, 120, 500]
discounted = map(lambda x: x * 0.9, prices)
filtered = filter(lambda x: x >= 200, discounted)
total = reduce(lambda a, b: a + b, filtered)
print(total)

#6.
from functools import reduce
scores = [80, 90, 70]
weights = [0.3, 0.5, 0.2]
weighted_score = reduce(
    lambda acc, pair: acc + pair[0] * pair[1],
    zip(scores, weights),
    0
)
print(weighted_score)

#7.
def count_up_to(n):
    for i in range(1, n + 1):
        yield i
for num in count_up_to(5):
    print(num)

#8.
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
f = fib()
for _ in range(10):
    print(next(f))

#9.
import itertools
def multiples_of_5():
    n = 1
    while True:
        yield n * 5
        n += 1
first_five = list(itertools.islice(multiples_of_5(), 5))
print(first_five)

#10.
total = sum(i*i for i in range(1, 10))
print(total)

