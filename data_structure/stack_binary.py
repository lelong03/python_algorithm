from stack import Stack


def decimal_to_binary(number):
    s = Stack()
    while number > 0:
        s.push(number % 2)
        number = number // 2

    result = ""
    while not s.is_empty():
        result = "%s%s" % (result, s.pop())
    return result


def base_convert(base, number):
    s = Stack()
    while number > 0:
        s.push(number % base)
        number = number // base
    digits = "0123456789ABCDEF"
    result = ""
    while not s.is_empty():
        result = "%s%s" % (result, digits[s.pop()])
    return result


print decimal_to_binary(233)
print base_convert(8, 233)
print base_convert(2, 233)
print base_convert(16, 233)
print hex(233)
