import sys

def factorial(n):
    answer = 1
    for i in range(1, n+1):
        answer *= i
    return answer


T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())

    if N % 2:
        print(0)
        
    else:
        n = N//2
        answer = (factorial(N)//(factorial(n)*factorial(n)*(n+1)))
        print(answer % 1000000007)
