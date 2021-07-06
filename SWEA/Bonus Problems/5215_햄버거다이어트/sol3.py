# 오답
import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, L = map(int, input().split())
    val = []
    cal = []
    total_v = []
    total_c = []

    for _ in range(N):
        v, c = map(int, input().split())
        val.append(v)
        cal.append(c)

    for i in range(N):
        if cal[i] <= L:
            total_v.append([val[i]])
        else:
            total_v.append([0])
        total_c.append([cal[i]])

    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            max_v = max(total_v[j])
            check = False
            for k in range(len(total_v[j])):
                if total_c[j][k] + cal[i] <= L and total_v[j][k] + val[i] >= max_v:
                    check = True
                    max_v = total_v[j][k] + val[i]
                    max_c = total_c[j][k] + cal[i]
            if check:
                total_v[j].append(max_v)
                total_c[j].append(max_c)

    ans = max(total_v[0])
    for i in range(1, N):
        if max(total_v[i]) > ans:
            ans = max(total_v[i])

    # print(total_c)
    # print(total_v)
    print("#{} {}".format(tc, ans))

