import sys
sys.stdin = open('sample_input.txt')


# 병합 정렬 함수
def merge_sort(arr):
    global cnt
    length = len(arr) # 인자로 들어오는 리스트의 길이를 따로 저장

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

    # 왼쪽 리스트의 마지막 수가 오른쪽 리스트의 마지막 수보다 클 경우 cnt 1 증가
    if sorted_left[-1] > sorted_right[-1]:
        cnt += 1

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


# main
T = int(input())

for tc in range(1, T+1):
    # 리스트의 크기와 리스트 입력 받기
    N = int(input())
    numbers = list(map(int, input().split()))

    # 경우의 수를 셀 변수 cnt
    cnt = 0
    # 병합 정렬 실시
    sorted_numbers = merge_sort(numbers)

    # 정답 출력
    print("#{} {} {}".format(tc, sorted_numbers[N//2], cnt))


