import sys

# 입력 받아 무게, 가치를 모아서 보관하는 리스트 생성
N, K = map(int, sys.stdin.readline().split())
weight = []
value = []
for i in range(N):
    W, V = map(int, sys.stdin.readline().split())
    weight.append(W)
    value.append(V)

# 테이블 초기화
table = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        # weigth의 값이 현재 비교하는 무게 이하일 경우
        # '이전 table의 값'과 '과거 조합 + 현재 value의 합' 중 어느 것이 더 큰 지 비교
        if weight[i-1] <= j:
            temp = value[i-1] + table[i-1][j-weight[i-1]]
            if temp > table[i-1][j]:
                table[i][j] = temp
            else:
                table[i][j] = table[i-1][j]
        # weigth의 값이 현재 비교하는 무게 이상일 경우
        # 비교 범위를 벗어나므로 이전 값을 그대로 가져온다
        else:
            table[i][j] = table[i-1][j]
            
# 테이블의 마지막 원소 출력
print(table[N][K])
