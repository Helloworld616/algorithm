# 다른 친구 코드 1

T = int(input())
for tc in range(1, T + 1):
    n, l = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(n)]

    result = 0
    for i in range(1 << n):
        t = k = 0
        for j in range(n):
            if i & (1 << j):
                t += info[j][0]
                k += info[j][1]
                if k > l:
                    break

        if k <= l and t > result:
            result = t

    print('#{} {}'.format(tc, result))