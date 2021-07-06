def powerset(idx, arr, N):
    if idx == N:
        total = 0
        p_set = []
        for i in range(N):
            if sel[i]:
                total += arr[i]
                p_set.append(arr[i])
        if total == 10:
            print(p_set)
    else:
        sel[idx] = 1
        powerset(idx + 1, arr, N)
        sel[idx] = 0
        powerset(idx + 1, arr, N)


arr = [i for i in range(1, 11)]
sel = [0] * len(arr)
powerset(0, arr, len(arr))
