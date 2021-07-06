# import sys
# sys.stdin = open('sample_input.txt')

T = int(input())

for i in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    answers = []
    for idx1 in range(N-M+1):
        total = 0
        for idx2 in range(idx1, idx1+M):
            total += numbers[idx2]
        answers.append(total)
    max_num = answers[0]
    min_num = answers[0]
    for idx in range(1, len(answers)):
        if max_num < answers[idx]:
            max_num = answers[idx]
        if min_num > answers[idx]:
            min_num = answers[idx]
    print('#{} {}'.format(i, max_num - min_num))