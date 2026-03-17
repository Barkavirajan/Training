def is_balanced(s):
    stack = []
    
    mapping = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        if char in "({[":
            stack.append(char)
        else:
            if not stack or stack.pop() != mapping[char]:
                return False

    return len(stack) == 0


# Test
print(is_balanced("({[]})"))  # True
print(is_balanced("([)]"))    # False