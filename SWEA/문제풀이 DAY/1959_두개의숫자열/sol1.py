import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if len(A) > len(B):
        long = A
        short = B
        short_num = M

    else:
        long = B
        short = A
        short_num = N

    answers = []
    for i in range(len(long)-len(short)+1):
        answer = 0
        for j in range(short_num):
            answer += long[i+j] * short[j]
        answers.append(answer)

    result = answers[0]
    for i in range(1, len(answers)):
        if answers[i] > result:
            result = answers[i]

    print('#{} {}'.format(tc, result))