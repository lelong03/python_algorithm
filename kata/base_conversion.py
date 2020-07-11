

bin      = '01'
oct      = '01234567'
dec      = '0123456789'
hex      = '0123456789abcdef'
allow    = 'abcdefghijklmnopqrstuvwxyz'
allup    = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha    = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphanum = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def convert(input, source, target):
    target_len = len(target)
    if input.isdigit():
        number = int(input)
        result = []
        while number > 0:
            temp = number % target_len
            result.append("%s" % target[temp])
            number = number / target_len
        result.reverse()
        return "".join(result)
    return "LONG"


print convert("15", dec, bin)       #==>  "1111"
print convert("15", dec, oct)       #==>  "17"
print convert("1010", bin, dec)     #==>  "10"
print convert("1010", bin, hex)     #==>  "a"
print convert("0", dec, alpha)      #==>  "a"
print convert("27", dec, allow)     #==>  "bb"
print convert("hello", allow, hex)  #==>  "320048"