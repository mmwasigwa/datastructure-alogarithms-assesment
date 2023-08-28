# Question 1: Implement a function is_balanced(expression) that takes a string 
# containing parentheses, curly braces, and square brackets,and determines whether 
# the expression is balanced. 

def is_balanced(string):
    stack_list = []

    opening_symbols = {"{", "(", "["}
    closing_symbols = {"}", ")", "]"}
    symbol_mapping = {')': '(', '}': '{', ']': '['}

    

    for char in string:
        if char in opening_symbols:
            stack_list.append(char)
        elif char in closing_symbols:
            if not stack_list or stack_list[-1] != symbol_mapping[char]: 
                return False  # Unbalanced if no matching opening symbol on stack
            stack_list.pop()  # Remove the matching opening symbol from the stack
    
    return len(stack_list) == 0  # If the stack is empty, the string is balanced

# Test cases
print(is_balanced("()"))  # True
print(is_balanced("{[()]}"))  # True
print(is_balanced("{[(])}"))  # False
print(is_balanced("([)]"))  # False