a = [1,2,2,2,4,4,4,4,5,5,5,5,5,7,7,8,8,8,8]

def get_nth_number(adict, n):
    alist = adict.items()
    count  = 0
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i][1] > alist[i+1][1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
        count += 1
        if count == n:
            return alist[passnum]
    return alist[0]

def convert_to_dict(alist):
    result = {}
    for item in alist:
        if item not in result:
            result[item] = 1
        else:
            result[item] += 1
    return result

def solve(alist):
    adict = convert_to_dict(alist)
    return get_nth_number(adict, 4)

tup = solve(a)
print "most frequent number is: %s" % tup[0]
print "number of times: %s" % tup[1]