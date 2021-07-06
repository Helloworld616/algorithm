def solution(jobs):
    N = len(jobs)
    jobs.sort(key=lambda x: x[1])
    print(jobs)

    start = jobs[0][0]
    time = jobs[0][1]
    idx = 0

    for i in range(1, N):
        if jobs[i][0] < start:
            start = jobs[i][0]
            time = jobs[i][1]
            idx = i
        elif jobs[i][0] == start and jobs[i][1] < time:
            time = jobs[i][1]
            idx = i

    finish = start + time
    total = time
    # print(total)
    checked = [False] * N
    checked[idx] = True

    while True:
        # print(checked)
        flag = True

        for i in range(N):
            if jobs[i][0] <= finish and not checked[i]:
                checked[i] = True
                flag = False
                finish += jobs[i][1]
                total += finish - jobs[i][0]
                # print(total)

        if flag:
            tmp_start = float('inf')
            tmp_time = float('inf')
            tmp_idx = 0
            for i in range(N):
                if jobs[i][0] < tmp_start and not checked[i]:
                    tmp_start = jobs[i][0]
                    tmp_time = jobs[i][1]
                    tmp_idx = i

            checked[tmp_idx] = True
            finish = tmp_start + tmp_time
            total += tmp_time
            # print(total)

        if False not in checked:
            break

    return total // N


# print(solution([[0, 3], [1, 9], [2, 6]]))  # 9
print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]))  # 72

