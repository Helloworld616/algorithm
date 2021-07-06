import sys
sys.stdin = open('s_input.txt')


T = int(input())
for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())
    answer = F * D/(A+B)
    print('#%d %.10f' % (tc, answer))