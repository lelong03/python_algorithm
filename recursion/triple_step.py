# A child is running up a staircse with n steps and can hop either 1 step, 2 steps, or 3 steps at a time.
# Implement a method to count how many possible ways the child can run up the stairs

import time


# Brute Force
def count_ways(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return count_ways(n-1) + count_ways(n-2) + count_ways(n-3)


# start_time = time.time()
# print(count_ways(20))
# print(time.time() - start_time)


# Using memoize
def count_ways_memoize(n, cache):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n not in cache:
        cache[n] = count_ways_memoize(n-1, cache) + count_ways_memoize(n-2, cache) + count_ways_memoize(n-3, cache)
    return cache[n]


start_time = time.time()
print(count_ways_memoize(500, {}))
print(time.time() - start_time)


