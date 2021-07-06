# 라이브강의 해설
import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N : 숫자의 갯수, M : 이동할 횟수
    queue = input().split()

    M = M % N

    print('#{} {}'.format(tc, queue[M]))