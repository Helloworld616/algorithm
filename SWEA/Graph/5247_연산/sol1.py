import sys
from collections import deque
sys.stdin = open("sample_input.txt")


# bfs 함수
def bfs():
    # 큐 생성
    queue = deque()
    # 첫 번째 자연수 N과 횟수 넣기
    queue.append((N, 0))

    # 방문 배열 생성. 케이스 최댓값이 백만이므로 (백만 + 1)만큼의 공간을 만든다.
    # 이미 한 번 나온 숫자는 방문 체크를 해서 같은 연산을 또 다시 수행하기 않게 하기 위함이다!
    visited = [False] * 1000001
    # 첫 번쨰 자연수 방문 체크
    visited[N] = True

    # bfs 시작
    while queue:
        # 큐에서 원소를 꺼내서 숫자와 횟수를 받는다.
        info = queue.popleft()
        number = info[0]
        cnt = info[1]

        # 만약 숫자가 M일 경우 bfs를 종료하고 횟수 반환
        if number == M:
            return cnt

        # bfs 탐색 후보들을 리스트로 생성
        candidates = [number+1, number-1, number*2, number-10]

        # 후보를 하나씩 꺼낸다.
        for candidate in candidates:
            # 만약 후보가 백만 이하이고, 아직 연산하지 않은 결과일 경우
            if 0 < candidate <= 1000000 and not visited[candidate]:
                # 방문 체크를 하고
                visited[candidate] = True
                # 연산 횟수에 1을 더해서 후보와 함께 큐에 넣는다.
                queue.append((candidate, cnt+1))


# main
T = int(input())

for tc in range(1, T+1):
    # 자연수 N, M 입력 받기
    N, M = map(int, input().split())
    # bfs 탐색 결과 출력
    print("#{} {}".format(tc, bfs()))

