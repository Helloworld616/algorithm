import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


"""
이차원 dp 배열을 만든 뒤, 첫 번째 행에 Base Case를 채운다.
그리고 두 번째 행부터 직전 행으로부터 파생되는 값들을 모두 체크하고,
마지막 행에서 체크 된 인덱스 중 값이 가장 큰 것을 출력하면 된다.

* 주의 : 체크되는 값이 없으면 -1을 반환하는 것을 잊지 말아야 한다!

"""


# 최대 볼륨을 반환하는 함수
def max_volume(dp):
    # Base Case 할당
    # Base Case가 아무것도 없으면 -1 반환
    if S + V[0] <= M:
        dp[0][S + V[0]] = True
    if S - V[0] >= 0:
        dp[0][S - V[0]] = True

    # dp 배열 채우기
    # 직전 행에서 체크된 값으로부터 볼륩을 키우고, 줄인 값을 이번 행에 저장한다.
    # 이번 행에 저장한 값이 아무것도 없으면 -1 반환
    for i in range(1, N):
        for j in range(M+1):
            if dp[i - 1][j] and j + V[i] <= M:
                dp[i][j + V[i]] = True
            if dp[i - 1][j] and j - V[i] >= 0:
                dp[i][j - V[i]] = True

    # 곡을 끝까지 연주하였을 경우
    # 마지막 행에서 체크된 값 중 가장 큰 것을 max_volume에 저장
    max_volume = -1
    for volume in range(M+1):
        if dp[N-1][volume] and volume > max_volume:
            max_volume = volume

    # max_volume 반환
    return max_volume



# main
# 입력 받기
N, S, M = map(int, input().split())
V = list(map(int, input().split()))

# 이차원 dp 배열 생성
# N과 M의 범위 주의!
dp = [[False]*(M+1) for _ in range(N)]

# 최대 볼륨값 출력
print(max_volume(dp))


