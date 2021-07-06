# 라이브강의 해설 2

T = int(input())

for tc in range(1, T + 1):
    # N : 원소의 갯수
    # M : 구간의 길이
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    max_value = 0
    min_value = 987654321

    # 중복된 연산을 피하자
    tmp = 0

    # 첫 구간은 구해놓자
    for i in range(M):
        tmp += nums[i]

    max_value = tmp
    min_value = tmp

    for i in range(M, N):
        # 새로운 구간의 합을 아주 간단하게 구할 수 있음
        tmp = tmp + nums[i] - nums[i - M]

        if max_value < tmp:
            max_value = tmp
        if min_value > tmp:
            min_value = tmp

    print('#{} {}'.format(tc, max_value - min_value))
