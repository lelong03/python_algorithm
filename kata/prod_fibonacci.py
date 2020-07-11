def productFib(prod):
    prev, current = 0, 1
    while prev * current < prod:
        prev, current = current, current + prev
    return [prev, current, current * prev == prod]

print productFib(800)