# 다른 친구 코드 2

def diet(idx, t, k):
    global result

    if k > l:
        return

    if idx == n:
        if t > result:
            result = t
        return

    diet(idx + 1, t + info[idx][0], k + info[idx][1])
    diet(idx + 1, t, k)


T = int(input())
for tc in range(1, T + 1):
    n, l = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(n)]

    result = 0
    diet(0, 0, 0)

    print('#{} {}'.format(tc, result))