def valid_parentheses(str):
    stack = []
    for c in str:
        if c == "(":
            stack.append(c)
        if c == ")":
            if len(stack) == 0:
                return False
            stack.pop()
    if len(stack):
        return False
    return True


print valid_parentheses("  (")
print valid_parentheses(")test")
print valid_parentheses("hi(hi)()")
print valid_parentheses("")