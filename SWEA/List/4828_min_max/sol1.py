# import sys
# sys.stdin = open('sample_input.txt')

T = int(input())

for i in range(1, T+1):
    tc = int(input())
    numbers = list(map(int, input().split()))
    max_num = min_num = numbers[0]
    for idx in range(1, len(numbers)):
        if numbers[idx] > max_num:
            max_num = numbers[idx]
        if numbers[idx] < min_num:
            min_num = numbers[idx]
    print('#{} {}'.format(i, max_num - min_num))
