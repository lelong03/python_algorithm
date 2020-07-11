def pick_peaks(arr):
    pos = []
    peaks = []
    maybe = False
    peak = None
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            maybe = True
            peak = i
        elif arr[i] < arr[i-1] and maybe is True:
            pos.append(peak)
            peaks.append(arr[peak])
            maybe = False
    return {'pos': pos, 'peaks': peaks}


print pick_peaks([18, 11, 5, 14, 16, -1, 12, 12, 12, 1])