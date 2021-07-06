import sys
sys.stdin = open("sample_sample_input.txt")


def cal(row, col, height, visited):
    global ans

    for i in range(N):
        if not visited[i]:  # 아직 체크하지 않은 박스일 경우
            visited[i] = True  # 방문 체크

            # 현재 박스에서 나올 수 있는 면적들을 모두 확인해보자
            for j in range(len(idx)):
                # 현재 박스의 가로, 세로 길이가 바로 아래 박스의 가로, 세로 길이 이하인 경우
                if (boxes[i][idx[j][0]] <= row and boxes[i][idx[j][1]] <= col) or \
                        (boxes[i][idx[j][0]] <= col and boxes[i][idx[j][1]] <= row):
                    # 현재 박스를 쌓자
                    n_row = boxes[i][idx[j][0]]
                    n_col = boxes[i][idx[j][1]]
                    n_height = height + boxes[i][remain[j]]
                    # 쌓인 높이가 ans보다 높을 경우 ans 갱신
                    if n_height > ans:
                        ans = n_height

                    # 비교값 만들기
                    # 비교값을 현재 높이로 초기화
                    compare = n_height
                    # 아직 체크하지 않은 박스들의 최대 변을 비교값에 더한다.
                    for k in range(N):
                        if not visited[k]:
                            compare += max(boxes[k])

                    # 비교값이 ans보다 클 경우에만 다음 탐색 진행
                    if ans < compare:
                        cal(n_row, n_col, n_height, visited)

            visited[i] = False


# main
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    boxes = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    idx = [(0, 1), (0, 2), (1, 2)]
    remain = [2, 1, 0]
    ans = 0

    for box in boxes:
        max_height = max(box)
        if max_height > ans:
            ans = max_height

    cal(10000, 10000, 0, visited)

    print(f"#{tc} {ans}")
