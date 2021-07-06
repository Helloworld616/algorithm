import sys
sys.stdin = open('input.txt')

'''
* Merge Sort의 기본 아이디어
  1. Divide O(1)
  2. Conquer O(logN)
  3. Combine O(N)
  ∴ Comebine이 Conquer 과정 안에서 일어나므로 Merge Sort의 최종 시간 복잡도는 O(NlogN)이다.
  
원소가 하나만 남을 때까지 Divide & Conquer를 계속한다.
원소가 다 나뉘어지면 대소비교를 하면서 Combine 한다.

이 코드는 Merge Sort로 오름차순 정렬을 구현하였다.

'''

# Merge 함수
# Comnine을 수행함
# 리스트를 복제하여 원본 리스트와 값을 비교해가며 정렬한다.
def merge(arr, left, middle, right):
    # 원본 리스트의 첫 인덱스 저장
    arr_idx = left
    # 복제 리스트의 첫 인덱스, 끝 인덱스 저장
    left_idx = left
    right_idx = middle + 1

    # 리스트 복제
    clone = arr[:]

    # left_idx가 중간값보다 작고, right_idx가 마지막 값보다 작을 경우에만 시행
    while left_idx <= middle and right_idx <= right:
        # 왼쪽 값이 오른쪽 값보다 작을 경우 할당
        if clone[left_idx] < clone[right_idx]:
            arr[arr_idx] = clone[left_idx]
            left_idx += 1
        # 오른쪽 값이 왼쪽 값보다 작을 경우 할당
        # 이렇게 작은 값들이 먼저 할당되므로 자연스럽게 오름차순이 형성된다.
        else:
            arr[arr_idx] = clone[right_idx]
            right_idx += 1
        arr_idx += 1

    # 만약 미처 다 할당하지 못하고 남은 부분들이 있다면 모두 할당한다
    while left_idx <= middle:
        arr[arr_idx] = clone[left_idx]
        arr_idx += 1
        left_idx += 1

    while right_idx <= right:
        arr[arr_idx] = clone[right_idx]
        arr_idx += 1
        right_idx += 1


# Merge Sort 함수
# Divide & Conquer를 수행
def merge_sort(arr, left, right):
    # 왼쪽 인덱스가 오른쪽 인덱스보다 작을 때에만 수행
    # 오른쪽 인덱스가 더 크면 Divide가 올바르게 이루어지지 않기 때문이다.
    if left < right:
        # 중간값 구하기
        middle = (left + right) // 2
        # 중간값을 기준으로 인덱스 나누기
        merge_sort(arr, left, middle)
        merge_sort(arr, middle+1, right)
        # 더 이상 나눌 수가 없게 되면 Combine
        merge(arr, left, middle, right)


# main
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    merge_sort(arr, 0, len(arr)-1)
    print('#{} {}'.format(tc, ' '.join(list(map(str, arr)))))