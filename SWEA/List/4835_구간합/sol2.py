# 라이브강의 해설 1

T = int(input())

for tc in range(1, T+1):
    # N : 원소의 갯수
    # M : 구간의 길이
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    max_value = 0
    min_value = 987654321

    # 구간 시작점
    for i in range(N - M + 1):
        tmp = 0

        for j in range(M):
            tmp += nums[i + j]
        # for i in nums[i:i+M]:
        #     tmp += j

        # 큰 값 갱신
        if max_value < tmp:
            max_value = tmp

        # 작은 값 갱신
        if min_value > tmp:
            max_value = tmp

    print('#{} {}'.format(tc, max_value-min_value))