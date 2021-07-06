import sys
sys.stdin = open("input.txt")

# 전역변수 무한대 선언
INF = float('inf')


# 치킨 거리 구하는 함수
def cal_distance():
    # 거리를 0으로 초기화
    distance = 0

    # 집의 좌표를 담은 리스트 houses의 인덱스 하나씩 꺼내기
    for i in range(H):
        # 결과값 초기화
        result = INF
        # 치킨집의 좌표를 담은 chickens의 인덱스 하나씩 꺼내기
        for j in range(C):
            # 고른 치킨집일 경우에만 연산 수행
            if chosen[j]:
                # 집과 치킨집 사이의 거리 구하기
                compare = abs(houses[i][0] - chickens[j][0]) + abs(houses[i][1] - chickens[j][1])
                # 구한 거리가 결과값보다 작을 경우, 결과값 갱신
                if compare < result:
                    result = compare
        # 치킨 거리에 결과값 추가. 결과값은 최솟값으로 갱신된 상태임
        distance += result

    # 최종적으로 산출된 치킨 거리 반환
    return distance


# 완전탐색 함수
# start : 탐색 시작 지점
# choose : 고른 치킨집의 수
def choose_chickens(start, choose):
    global min_distance

    if choose == M:
        """
        종료 조건 : M개의 치킨집을 골랐을 때
        
        * 중요!!!
          치킨 거리의 최솟값은 치킨집을 없앨수록 줄어듭니다! (경우의 수가 줄어들기 때문에)
          따라서 최대 M개를 고를 수 있다는 조건은 함정입니다-_-;;; M개 이하의 선택은 의미가 없습니다.
          이 조건에 속지 않고, M개를 고르는 순간 탐색을 멈춰야 시간 초과가 나지 않습니다! 
          
        """
        # 현재 고른 치킨집의 치킨 거리 구하기
        distance = cal_distance()
        # 치킨 거리가 최소 거리보다 작으면
        # 최소 거리를 치킨 거리고 갱신
        if distance < min_distance:
            min_distance = distance
    else:
        """
        실행 조건 : 아직 M개의 치킨집을 고르지 못했을 때
        """
        # 다음 치킨집을 고르고 선택 체크
        for i in range(start, C):
            chosen[i] = True
            choose_chickens(i+1, choose + 1)
            chosen[i] = False


# main
# 도시 크기, 선택할 치킨집 수, 도시 정보 입력 받기
N, M = map(int, input().split())
town = [list(map(int, input().split())) for _ in range(N)]

# 도시 정보를 담은 이차원 리스트 town을 순회하면서
# 집과 치킨집의 좌표를 찾아서 저장한다.
houses = []
chickens = []
for i in range(N):
    for j in range(N):
        if town[i][j] == 1:
            houses.append((i, j))
        if town[i][j] == 2:
            chickens.append((i, j))

# 집의 길이와 치킨집의 길이 저장 (이후에 계속 쓰이므로!)
H = len(houses)
C = len(chickens)

# 최소 거리와 선택 체크 배열 초기화
min_distance = INF
chosen = [False] * C

# 완전탐색 실시! 치킨집을 고르자!
choose_chickens(0, 0)

# 완전 탐색 결과 도출된 최소 거리 출력
print(min_distance)
