def first_non_repeating_letter(string):
    if len(string) == 0:
        return ''
    result = {}
    for c in string:
        c = c.lower()
        if c not in result:
            result[c] = 1
        else:
            result[c] = result[c] + 1
    for c in string:
        ct = c.lower()
        if result[ct] == 1:
            return c
    return ''



print first_non_repeating_letter('stress')
print first_non_repeating_letter('sesstr')
print first_non_repeating_letter('sTreSS')