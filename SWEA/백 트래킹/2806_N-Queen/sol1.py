import sys
sys.stdin = open('sample_input.txt')


# 백트래킹 함수
# qnum : 현재 퀸이 위치하는 체스판의 행
# location : 지금까지 퀸이 거쳐온 위치 정보를 담은 리스트
# cnt : 정답을 담은 리스트
# N : 체스판의 행/열 크기
def NQueen(qnum, location, cnt, N):
    if qnum == N:
        """
        종료조건 : 퀸이 체스판의 N번째 행까지 왔을 경우
        """
        cnt[0] += 1
    else:
        """
        실행조건 : 퀸이 아직 체스판의 N번째 행까지 도달하지 못했을 경우
        """
        # 0부터 (N-1)까지의 숫자들을 차례차례 꺼낸다.
        for i in range(N):
            # flag : 다음 탐색 실행 가능 여부
            # True로 초기화
            flag = True

            # 지금까지 거쳐온 위치 정보들을 하나씩 꺼낸다
            for j in location:
                # 1. 상하 검사 : 이전에 이미 탐색한 열인가?
                # 2. 대각선 검사 : (현재 행-이전 행)과 (현재 열-이전 열)이 같지는 않은가?
                if i == j[1] or abs(qnum-j[0]) == abs(i-j[1]):
                    # 둘 중 하나라도 걸리면 다음 탐색 불가
                    flag = False
                    break
            # 다음 탐색이 가능할 경우
            if flag:
                # 위치 정보를 담은 리스트에 현재 위치를 담고
                location.append((qnum, i))
                # 다음 탐색 고고씽
                NQueen(qnum+1, location, cnt, N)
                # 그 다음 위치 정보를 원래대로 되돌려놓는다!
                location.pop()


# main
T = int(input())

for tc in range(1, T+1):
    # 체스판의 크기 입력받기
    N = int(input())
    # 정답을 담은 cnt 배열을 생성하고 초기화
    cnt = [0]
    # 백트래킹 실시
    NQueen(0, [], cnt, N)
    # 정답 출력
    print('#{} {}'.format(tc, cnt[0]))
