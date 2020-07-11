def find_longest_increasing_subsequence(sequence):
    max_arr = [1] * len(sequence)
    for i in range(len(sequence)):
        for j in range(i):
            if sequence[j] <= sequence[i] and max_arr[j] + 1 > max_arr[i]:
                max_arr[i] = max_arr[j] + 1
    return max_arr

if __name__ == "__main__":
    # INPUT
    A = [5,3,4,8,6,7]

    # SOLVE
    result = find_longest_increasing_subsequence(A)

    # OUTPUT
    print(result)
