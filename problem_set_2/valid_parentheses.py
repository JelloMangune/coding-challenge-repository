def isValid(s):
    stack = []
    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack:
                return False
            top = stack.pop()
            if (char == ')' and top != '(') or (char == '}' and top != '{') or (char == ']' and top != '['):
                return False
    return len(stack) == 0

input_string1 = "()[]{}"
input_string2 = "([)]"
valid_input1 = "([]){}"
valid_input2 = "[{()}]"
invalid_input1 = "{[(]})"
invalid_input2 = "}(){"

print(isValid(input_string1))
print(isValid(input_string2))
