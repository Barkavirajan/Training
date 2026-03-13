def rotate_array(nums, k):
    n = len(nums)
    k = k % n
    nums.reverse()
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])
    return nums
arr = [1,2,3,4,5,6,7]
k = 3
print(rotate_array(arr, k))

#without using reverse

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
def rotate_array(arr, k):
    n = len(arr)
    k = k % n
    reverse(arr, 0, n-1)
    reverse(arr, 0, k-1)
    reverse(arr, k, n-1)
    return arr
arr = [1,2,3,4,5,6,7]
k = 3
print(rotate_array(arr, k))