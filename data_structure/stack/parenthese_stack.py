from pythonds.basic.stack import Stack

# simple parenthese like ()
def balanced_parenthese_checker(str):
    s = Stack()
    balanced = True
    index = 0

    while index < len(str) and balanced:
        ch = str[index]
        # incase "("
        if ch == "(":
            s.push(ch)

        # incase ")"
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False


print balanced_parenthese_checker('((()')
print balanced_parenthese_checker('((()))')
print balanced_parenthese_checker('((())()())')
print balanced_parenthese_checker('()()(()')
print "==================="



# advanced parenthese like (), {}, []
def adv_balanced_parenthese_checker(str):
    s = Stack()
    balanced = True
    index = 0

    while index < len(str) and balanced:
        ch = str[index]
        if ch in "([{":
            s.push(ch)
        else:
            if s.isEmpty():
                balanced = False
            else:
                previous = s.pop()
                if not is_matched(previous, ch):
                    balanced = False
        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False


def is_matched(open_ch, close_ch):
    opens = '([{'
    closes = ')]}'
    return opens.index(open_ch) == closes.index(close_ch)


print adv_balanced_parenthese_checker('([]{})')
print adv_balanced_parenthese_checker('({}[]({]}))')
print adv_balanced_parenthese_checker('({}[]({}))')
print adv_balanced_parenthese_checker('()()[][()')