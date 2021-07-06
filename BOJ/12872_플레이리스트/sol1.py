import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


# 결과 도출 함수
# length : 플레이리스트 길이
# pick : 고른 노래의 갯수
def cal(length, pick):
    # 고르지 않은 노래 갯수 계산
    unpick = N - pick

    # 현재 플레이리스트의 길이가 P라면
    if length == P:
        # 고르지 않은 노래가 없다면 1 반환
        if unpick == 0:
            return 1
        # 고르지 않은 노래가 있다면 0 반환
        else:
            return 0

    # 만약 dp에 현재 length와 pick에 해당하는 값이 이미 있다면 가져다가 사용
    if dp[length][pick] != -1:
        return dp[length][pick]

    # 정답 0으로 초기화
    ans = 0

    # 고르지 않은 노래가 있다면
    if unpick > 0:
        # 이 곡을 넣는 경우를 계산
        # 곡 하나가 증가하므로 pick이 1 늘어나야 하고
        # 플레이리스트의 길이도 1 증가해야 한다.
        ans += cal(length+1, pick+1) * unpick

    # 고른 노래의 갯수가 M개를 넘었다면
    if pick > M:
        # 끝에서부터 M+1번째 곡 ~ 첫 곡까지는 한 번 더 담겨도 된다!
        ans += cal(length+1, pick) * (pick - M)

    # 나머지 계산
    ans %= 1000000007
    # 최종 계산 값을 dp에 할당
    dp[length][pick] = ans
    # 정답 반환
    return ans


# main
# 입력 받기
N, M, P = map(int, input().split())
# 이차원 배열 dp 초기화
dp = [[-1 for _ in range(N+1)] for _ in range(P+1)]
# 결과 출력
print(cal(0, 0))