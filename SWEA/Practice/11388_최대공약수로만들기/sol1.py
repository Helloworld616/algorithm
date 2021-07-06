# 시간초과

import sys
sys.stdin = open('sample_input.txt')


T = int(input())

for tc in range(1, T+1):
    N, G = map(int, input().split())
    numbers = list(map(int, input().split()))
    cnt = 0
    for i in range(1, 1 << len(numbers)):
        subset = []
        for j in range(len(numbers)+1):
            if i & 1 << j:
                subset.append(numbers[j])

        factor = []
        for num in range(1, subset[0]+1):
            if subset[0] % num == 0:
                factor.append(num)

        for idx in range(1, len(subset)):
            temp = []
            for num in range(1, subset[idx]+1):
                if subset[idx] % num == 0:
                    temp.append(num)
            factor = set(factor) & set(temp)

        factor = list(factor)
        max_factor = factor[0]
        for i in range(1, len(factor)):
            if factor[i] > max_factor:
                max_factor = factor[i]

        if max_factor == G:
            cnt += 1


    print('#{} {}'.format(tc, cnt % 1000000007))





