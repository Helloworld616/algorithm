# 재귀

"""
모든 부분 집합을 구하는 함수
그 중에서 원소의 총합이 10이 되는 경우를 출력
"""


# length : 현재 부분집합의 길이
# start : 반복문의 시작 인덱스
# powerset : 부분집합을 담을 리스트
def perm(length, start, powerset):
    # 실행 조건 : 현재 부분집합의 길이가 원본 리스트의 길이보다 작을 경우
    if length < N:
        # 반복문에서 인덱스를 하나씩 꺼낸다.
        for i in range(start, N):
            # 인덱스에 해당하는 원소를 원본리스트에서 가져와서 부분 집합에 추가
            powerset.append(arr[i])
            # 부분집합 원소의 총합이 10이 되는 경우 출력
            if sum(powerset) == 10:
                print(powerset)
            # 다음 탐색 실시
            perm(length+1, i+1, powerset)
            # 부분집합 되돌려놓기
            powerset.pop()


# main
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # 주어진 리스트
N = len(arr)  # 리스트의 길이 저장
perm(0, 0, [])  # 조건을 만족하는 부분집합 출력
