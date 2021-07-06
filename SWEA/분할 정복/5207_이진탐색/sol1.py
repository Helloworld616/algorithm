import sys
sys.stdin = open('sample_input.txt')


# 병합 정렬 함수
def merge_sort(arr):
    # 인자로 들어오는 리스트의 길이를 따로 저장
    length = len(arr)

    # 리스트의 길이가 2보다 작을 경우 바로 반환
    if length < 2:
        return arr

    # 중간 인덱스를 구한 후
    # 중간 인덱스를 기준으로 왼쪽 리스트와 오른쪽 리스트로 나눔
    mid_idx = length // 2
    left = arr[:mid_idx]
    right = arr[mid_idx:]

    # 왼쪽 리스트와 오른쪽 리스트를 각각 병합 정렬
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    # 왼쪽 리스트와 오른쪽 리스트의 병합 결과를 담을 리스트 merge 생성
    merged = []
    # 왼쪽 리스트 접근 인덱스 l_idx와
    # 오른쪽 리스트 접근 인덱스 r_idx를
    # 0으로 초기화
    l_idx = r_idx = 0

    # l_idx가 정렬된 왼쪽 리스트의 길이보다 작고
    # r_idx가 정렬된 오른쪽 리스트의 길이보다 작을 경우
    # 계속 상호 비교 및 병합 실시
    while l_idx < len(sorted_left) and r_idx < len(sorted_right):
        if sorted_left[l_idx] < sorted_right[r_idx]:
            merged.append(sorted_left[l_idx])
            l_idx += 1
        else:
            merged.append(sorted_right[r_idx])
            r_idx += 1

    # 위 과정에서 미처 병합되지 않은 원소들이 있을 경우
    # 그 원소들도 병합
    merged += sorted_left[l_idx:]
    merged += sorted_right[r_idx:]

    # 병합 완료된 리스트 반환
    return merged


# 이진 탐색 함수
def binary_search(element, left, right):
    global is_left
    global is_right

    # 왼쪽 인덱스가 오른쪽 인덱스보다 작을 경우
    # 조건 검사 및 이진 탐색 실시
    if left <= right:
        # 중간 인덱스 구하기
        middle = (left + right) // 2

        # 숫자를 찾았을 경우 1 반환
        if element == A[middle]:
            return 1
        # 숫자가 A의 중간 인덱스 수보다 작을 경우 (= 왼쪽 탐색)
        elif element < A[middle]:
            # 직전에 왼쪽을 탐색했을 경우 0 반환
            if is_left:
                return 0
            # 아닐 경우, 왼쪽을 탐색했음을 표시한 후 다음 이진탐색 실시
            else:
                is_left = True
                is_right = False
                return binary_search(element, left, middle-1)
        # 숫자가 A의 중간 인덱스 수보다 클 경우 (= 오른쪽 탐색)
        else:
            # 직전에 오른쪽을 탐색했을 경우 0 반환
            if is_right:
                return 0
            # 아닐 경우, 오른쪽을 탐색했음을 표시한 후 다음 이진탐색 실시
            else:
                is_right = True
                is_left = False
                return binary_search(element, middle+1, right)

    # 아무런 조건도 만족하지 못할 경우 바로 0 반환
    return 0


# main
for tc in range(1, int(input())+1):
    # 리스트 A, B의 크기를 나타내는 수 N, M 입력받기
    N, M = map(int, input().split())
    # 리스트 A를 입력 받은 후 정렬
    A = merge_sort(list(map(int, input().split())))
    # 리스트 B 입력 받기
    B = list(map(int, input().split()))

    # 조건을 만족하는 수를 셀 변수 cnt
    cnt = 0
    # 리스트 B에서 숫자를 하나씩 꺼내서 점검
    for number in B:
        # 왼쪽 탐색/오른쪽 탐색 여부를 체크할 변수 is_left, is_right 생성
        is_left = False
        is_right = False
        # 조건을 만족할 경우 1을 더하고
        # 조건을 만족하지 않을 경우 0을 더한다.
        cnt += binary_search(number, 0, len(A)-1)

    # 정답 출력
    print('#{} {}'.format(tc, cnt))
