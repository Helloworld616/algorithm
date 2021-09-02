import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


# LIS의 길이를 구하는 함수
def max_length():
    # dp 리스트를 모두 1로 초기화
    dp = [1] * N

    # 1. 리스트 numbers 안의 숫자들을 하나씩 꺼내서
    # 2. 그 숫자들보다 인덱스와 값이 작은 수들의 dp 값을 확인하여 비교한다.
    for i in range(N):
        for j in range(i):
            if numbers[j] <= numbers[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    # dp 리스트의 최대값 반환
    return max(dp)


# main
N = int(input())  # 숫자의 갯수 N 입력 받기
numbers = [int(input()) for _ in range(N)]  # 숫자들을 입력 받아서 리스트에 담기
print(N - max_length())  # N에서 LIS의 길이를 뺀 값이 정답



