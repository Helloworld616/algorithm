import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())
    clerks = list(map(int, input().split()))

    dp = [False] * (sum(clerks) + 1)
    dp[0] = True

    for clerk in clerks:
        for i in range(len(dp)-1, -1, -1):
            if dp[i]:
                dp[i + clerk] = True

    ans = 0
    for i in range(B, len(dp)):
        if dp[i]:
            ans = i - B
            break

    print('#{} {}'.format(tc, ans))
