#1.Remove duplicates keeping the last occurrences

def remove_duplicates_keep_last(lst):
    seen = set()
    result = []
    for i in reversed(lst):
        if i not in seen:
            seen.add(i)
            result.append(i)
    return result[::-1]
lst = [1, 2, 3, 2, 4, 1, 5]
print(remove_duplicates_keep_last(lst))  

#2. Find the index of the second largest element in a list

def second_largest_index(lst):
    unique = list(set(lst))
    if len(unique) < 2:
        return -1
    unique.sort(reverse=True)
    second_largest = unique[1]
    return lst.index(second_largest)
lst = [4, 1, 3, 4, 2]
print(second_largest_index(lst))

#3. Convert list into tuple pairs

def list_to_tuple_pairs(lst):
    result = []
    for i in range(0, len(lst), 2):
        result.append((lst[i], lst[i+1]))
    return result
lst = [1, 2, 3, 4, 5, 6]
print(list_to_tuple_pairs(lst))

#4.Sorted unique words ignoring case
def sorted_uniquewords(text):
    words = text.lower().split()
    unique_words = sorted(set(words))
    return unique_words
text = "Hello world hello Python world"
print(sorted_uniquewords(text))

#5. Square of even numbers in a list
def square_even_num(lst):
    result = []
    for i in lst:
        if i%2 == 0:
            result.append(i*i)
    return result
lst = [1, 2, 3, 4, 5, 6]
print(square_even_num(lst))

#6.Password Check(attempt 3, successful - unlocked else - locked)
def password_check(password):
    attempts = 3
    while attempts > 0:
        current_password = input("Enter password: ")
        if current_password == password:
            return "Unlocked"
        else:
            attempts -= 1
    return "Locked"
print(password_check("admin123"))

#7. Interleave two lists
def interleave_lists(lst1, lst2):
    result = []
    min_length = min(len(lst1), len(lst2))
    for i in range(min_length):
        result.append(lst1[i])
        result.append(lst2[i])
    return result
lst1 = [1, 2, 3]
lst2 = ['a', 'b', 'c', 'd']
print(interleave_lists(lst1,lst2))

#8. Rotate list to the right by k positions
def rotate_list(lst, k):
    n = len(lst)
    k = k % n
    for _ in range(k):
        last = lst.pop()
        lst.insert(0, last)
    return lst
lst = [1, 2, 3, 4, 5]
k = 2
print(rotate_list(lst, k))

#9.Track running maximum in a list
def running_max(lst):
    result = []
    current_max = 0
    for i in lst:
        if i <= 0:
            current_max = 0
        else:
            current_max = max(current_max, i)
        result.append(current_max)
    return result
lst = [2, 1, -5, 3, 4, -9, -3]
print(running_max(lst))
    
#10. Compute cummulative sum of a list
def cumulative_sum(lst):
    result = []
    total = 0
    for x in lst:
        if x < 0:
            break
        total += x
        result.append(total)
    return result
lst = [1, 2, 3, -1, 4, 5]
print(cumulative_sum(lst))


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