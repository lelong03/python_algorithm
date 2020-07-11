from stack import Stack


def check_parenthese(str):
    m = Stack()
    index = 0

    while index < len(str):
        if str[index] == "(":
            m.push(str[index])
        else:
            if m.is_empty():
                return False
            m.pop()
        index = index + 1

    if m.is_empty():
        return True
    else:
        return False


def adv_check_parenthese(str):
    opens = ["(", "[", "{"]
    closes = [")", "]", "}"]
    m = Stack()
    index = 0
    while index < len(str):
        if str[index] in opens:
            m.push(str[index])
        else:
            if m.is_empty():
                return False
            pre = m.peek()
            if opens.index(pre) != closes.index(str[index]):
                return False
            m.pop()
        index = index + 1

    if m.is_empty():
        return True
    else:
        return False


# pstr = "())))))"
# print check_parenthese(pstr)

pstr = "{{([][])}()}"
print adv_check_parenthese(pstr)