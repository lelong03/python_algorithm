def simplify(poly):
    num_str = "1234567890"
    poly = poly.replace("-", "+-")
    result = {}
    for equation in poly.split("+"):
        if equation == "":
            continue
        if equation.startswith("-"):
            equation = equation[1:]
            v1 = -1
        else:
            v1 = 1
        value = ""
        while equation[0] in num_str:
            value = value + equation[0]
            equation = equation[1:]
        if value == "":
            value = 1
        else:
            value = int(value)
        equation = "".join(sorted(equation))
        if equation in result:
            result[equation] = result[equation] + (value * v1)
        else:
            result[equation] = value * v1
    # print result
    str = ""
    for key in sorted(result.keys(),reverse=True):
        if result[key] == 0:
            continue
        if result[key] == 1:
            str = str + "+%s" % key
        elif result[key] == -1:
            str = str + "-%s" % key
        else:
            str = str + ("+%s%s" % (result[key], key))
    return str[1:] if str[0] == '+' else str

print simplify("dc+dcba")
print simplify("2xy-yx")
print simplify("-a+5ab+3a-c-2a")
print simplify("-abc+3a+2ac")
print simplify("xyz-xz")
print simplify("a+ca-ab")
print simplify("-abc+3a+2ac")