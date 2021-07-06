import sys
sys.stdin = open('sample_input.txt')


def partition(arr, start, end):
    # pivot을 시작 인덱스로 초기화
    pivot = start

    # 첫 인덱스부터 마지막 인덱스 직전까지 반복문 실행
    # 이 과정을 거쳐서 pivot-1까지는 마지막 인덱스보다 작은 수들만 모이게 된다!
    # 마지막으로 pivot이 위치한 수는 마지막 인덱스보다 크거나 같은 수!
    for i in range(start, end):
        # 현재 인덱스의 수가 끝 인덱스의 수보다 작을 경우
        if arr[i] < arr[end]:
            # 현재 인덱스의 수와 pivot 인덱스의 수를 교환
            arr[i], arr[pivot] = arr[pivot], arr[i]
            # pivot 1 증가
            pivot += 1

    # 마지막으로 pivot이 위치한 수는 마지막 인덱스보다 크거나 같은 수이므로
    # 정렬을 위해 pivot과 마지막 인덱스의 수를 교환
    # 이 과정을 거쳐 pivot 왼쪽의 수는 전부 pivot보다 작아지게 된다!
    # 이 교환은 반드시 이루어져야 하므로 조건문 바깥에서 실시
    arr[pivot], arr[end] = arr[end], arr[pivot]

    # pivot 반환
    return pivot


# 퀵 정렬 함수
def quick_sort(arr, start, end):
    # 끝 인덱스가 시작 인덱스보다 클 경우에 정렬 실시
    if end > start:
        # pivot 구하기
        pivot = partition(arr, start, end)
        # pivot을 기준으로 왼쪽 리스트와 오른쪽 리스트를 나누어서 퀵 정렬 실시
        quick_sort(arr, start, pivot-1)
        quick_sort(arr, pivot+1, end)


for tc in range(1, int(input())+1):
    # 리스트의 크기와 리스트 입력 받기
    N = int(input())
    A = list(map(int, input().split()))

    # 퀵 정렬 실시
    quick_sort(A, 0, len(A)-1)

    # 정답 출력
    print('#{} {}'.format(tc, A[N//2]))
