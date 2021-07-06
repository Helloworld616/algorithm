import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


# Quick Sort 구현에 필요한 partition을 반환하는 함수
def partition(arr, start, end):
    p = start

    for i in range(start, end):
        if arr[i] < arr[end]:
            arr[i], arr[p] = arr[p], arr[i]
            p += 1

    arr[p], arr[end] = arr[end], arr[p]

    return p


# Quick Sort 함수
def quicksort(arr, start, end):
    if (end - start) > 0:
        p = partition(arr, start, end)
        quicksort(arr, start, p-1)
        quicksort(arr, p+1, end)


# main
# 입력 받기
N = int(input())
K = int(input())
# 센서의 좌표를 입력 받을 때 중복을 미리 제거
sensor = list(set(list(map(int, input().split()))))

# 입력 받은 센서의 좌표를 정렬
quicksort(sensor, 0, len(sensor)-1)

# 정답을 0으로 초기화
ans = 0

# K가 센서의 길이보다 크기가 같거나 크면 정답을 바로 출력
if K >= len(sensor):
    print(ans)
# 아닐 경우
else:
    # 커버 범위를 저장할 리스트 boundary 생성
    boundary = []
    # 센서 위치 값이 차이를 boundary에 저장
    for i in range(1, len(sensor)):
        boundary.append(sensor[i] - sensor[i-1])

    # boundary를 정렬
    quicksort(boundary, 0, len(boundary) - 1)

    # boundary에서 가장 큰 원소들을 K-1개 만큼 빼주기
    # boundary 안의 값들을 최소화하기 위한 과정이다.
    while K-1:
        boundary.pop()
        K -= 1

    # boundary에 남은 값들을 ans에 합산
    for i in range(len(boundary)):
        ans += boundary[i]

    # ans 출력
    print(ans)