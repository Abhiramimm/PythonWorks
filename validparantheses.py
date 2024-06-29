def isValid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if stack == [] or mapping[char] != stack.pop():
                return False
        else:
            return False

    return not stack

# Example usage:
input_str = "{[()]}"

if isValid(input_str):
    print("Valid parentheses")
else:
    print("Invalid parentheses")
