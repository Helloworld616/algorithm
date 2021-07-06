import sys
sys.stdin = open('sample_input.txt')


T = int(input())


for tc in range(1, T+1):
    N = int(input())
    cnt = N // 10
    numbers = [1, 3]
    for i in range(2, cnt):
        numbers.append(numbers[i-2]*2 + numbers[i-1])
    print("#{} {}".format(tc, numbers[cnt-1]))